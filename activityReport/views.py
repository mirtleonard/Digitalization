from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from activityReport.forms import ActivityReportForm
from activityReport.models import ActivityReport
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q

# Create your views here.
@login_required
def viewActivityReport(request, report_id):
    report = get_object_or_404(ActivityReport, pk=report_id)
    return render(request, 'viewActivityReport.html', {'report' : report})

@login_required
def createActivityReport(request):
    if request.method == 'POST':
        form = ActivityReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Raportul a fost creat!")
            user = request.user
            user.reports += 1
            user.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.error(request, "Raportul nu a fost creat!")
    else:
        form = ActivityReportForm(initial = {'username' : request.user.get_username()})
    context = {
        'report' : form,
        'path' : 'createActivityReport',
    }
    return render(request, 'editReport.html', context)

@login_required
def updateActivityReport(request, report_id):
    if request.method == 'POST':
        form = ActivityReportForm(request.POST)
        if form.is_valid():
            messages.success(request, "Raportul a fost editat!")
            report = form.save(commit=False)
            report.id = report_id
            report.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.error(request, "Raportul nu a fost editat")
    else:
        report = get_object_or_404(ActivityReport, pk = report_id)
        form = ActivityReportForm(instance=report)
        if report.username != request.user.get_username():
            messages.error(request, "Doar creatorul poate edita formularul")
            return viewActivityReport(request, report_id)
    context = {
        'report' : form,
        'path' : str(report_id),
    }
    return render(request, 'editReport.html', context)

@login_required
def deleteActivityReport(request, report_id):
    report = get_object_or_404(ActivityReport, pk = report_id)
    if report.username != request.user.get_username():
        messages.error(request, "Doar creatorul poate șterge formularul")
        return viewReport(request, report_id)
    else:
        user = request.user
        user.reports -= 1
        user.save()
        ActivityReport.objects.filter(id = report_id).delete()
        messages.success(request, "Raportul a fost șters!")
        return HttpResponseRedirect(reverse('profile'))

@login_required
def searchActivityReports(request, branch):
    search = request.GET.get('search')
    if (not search):
        search = ""
    reports = ActivityReport.objects.filter(branch__icontains = branch)
    reports.filter(Q(title__unaccent__icontains = search) |
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
    context = {
        'reports':reports,
        'branch' : branch,
    }
    return render(request, 'searchActivityReports.html', context)
