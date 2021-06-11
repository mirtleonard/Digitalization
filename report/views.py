from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from report.forms import reportForm, EventReportForm
from django.contrib import messages
from report.models import Report
from django.urls import reverse
from django.db.models import Q

# Create your views here.
@login_required
def viewReport(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, 'viewReport.html', {'report': report})

@login_required
def createReport(request):
    if request.method == 'POST':
        form = reportForm(request.POST)
        if (form.is_valid()):
            report = form.save(commit=False)
            messages.success(request, "Raportul a fost creat!")
            user = request.user
            user.reports += 1
            user.save()
            report.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.error(request, "Raportul nu a fost creat!")
    else:
        form = reportForm(initial = {'username' : request.user.get_username()})
    context = {
        'report' : form,
        'path' : 'createReport',
        'type' : 'Activitate',
    }
    return render(request, 'editReport.html', context)

@login_required
def createEventReport(request):
    if request.method == 'POST':
        form = EventReportForm(request.POST)
        if (form.is_valid()):
            report = form.save(commit=False)
            messages.success(request, "Raportul a fost creat!")
            user = request.user
            user.reports += 1
            user.save()
            report.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.error(request, "Raportul nu a fost creat!")
    else:
        form = EventReportForm(initial = {'username' : request.user.get_username()})
    context = {
        'report' : form,
        'path' : 'createReport',
        'type' : 'Eveniment',
    }
    return render(request, 'editReport.html', context)

@login_required
def updateReport(request, report_id):
    if request.method == 'POST':
        form = reportForm(request.POST)
        if form.is_valid():
            messages.success(request, "Raportul a fost editat!")
            report = form.save(commit=False)
            report.id = report_id
            report.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.error(request, "Raportul nu a fost editat")
    else:
        report = get_object_or_404(Report, pk = report_id)
        form = reportForm(instance=report)
        if report.username != request.user.get_username():
            messages.error(request, "Doar creatorul poate edita formularul")
            return viewReport(request, report_id)
    context = {
        'report' : form,
        'path' : 'updateReport',
        'type' : 'Activitate',
    }
    return render(request, 'editReport.html', context)

@login_required
def deleteReport(request, report_id):
    report = get_object_or_404(Report, pk = report_id)
    if report.username != request.user.get_username():
        messages.error(request, "Doar creatorul poate șterge formularul")
        return viewReport(request, report_id)
    else:
        user = request.user
        user.reports -= 1
        user.save()
        Report.objects.filter(id = report_id).delete()
        messages.success(request, "Raportul a fost șters!")
        return HttpResponseRedirect(reverse('profile'))

@login_required
def searchReport(request):
    search = request.GET.get('search')
    if (not search):
        search = ""
    reports = Report.objects.filter(Q(title__unaccent__icontains = search) |
                                    Q(username__unaccent__icontains = search) |
                                    Q(branch__unaccent__icontains = search) |
                                    Q(date__icontains = search) |
                                    Q(description__unaccent__icontains = search) |
                                    Q(goals__unaccent__icontains = search) |
                                    Q(strengths__unaccent__icontains = search) |
                                    Q(weaknesses__unaccent__icontains = search) |
                                    Q(duration__unaccent__icontains = search) |
                                    Q(areas__unaccent__icontains = search) |
                                    Q(improvements__unaccent__icontains = search))
    if (not reports):
        reports = ""
    return render(request, 'searchReport.html', {'reports':reports})
