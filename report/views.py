from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from report.forms import reportForm
from report.models import Report
from django.urls import reverse
from django.db.models import Q

# Create your views here.
def viewReport(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, 'viewReport.html', {'report': report})

def createReport(request):
    if request.method == 'POST':
        form = reportForm(request.POST)
        if (form.is_valid()):
            report = form.save(commit=False)
            report.username = request.user.get_username()
            messages.success(request, "Raportul a fost creat!")
            user = request.user
            user.reports += 1
            user.save()
            report.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.error(request, "Raportul nu a fost creat!")
    else:
        form = reportForm()
    context = {
        'report' : form,
        'path' : 'createReport',
    }
    return render(request, 'editReport.html', context)


def updateReport(request, report_id):
    if request.method == 'POST':
        form = reportForm(request.POST)
        form.instance.username = request.user.get_username()
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
        'path' : "updateReport" ,
    }
    return render(request, 'editReport.html', context)



def searchReport(request):
    search = request.GET.get('search')
    filter
    if (not search):
        search = ""
    reports = Report.objects.filter(Q(title__icontains = search) |
                                    Q(username__icontains = search) |
                                    Q(branch__icontains = search) |
                                    Q(date__icontains = search) |
                                    Q(description__icontains = search) |
                                    Q(goals__icontains = search) |
                                    Q(strengths__icontains = search) |
                                    Q(weaknesses__icontains = search) |
                                    Q(duration__icontains = search) |
                                    Q(areas__icontains = search) |
                                    Q(improvements__icontains = search))
    if (not reports):
        reports = ""
    return render(request, 'searchReport.html', {'reports':reports})
