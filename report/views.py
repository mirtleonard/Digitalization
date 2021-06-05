from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from report.forms import reportForm
from report.models import Report
from django.urls import reverse
from django.db.models import Q

# Create your views here.
def saveReport(request):
    form = reportForm(request.POST)
    if (form.is_valid()):
        report = form.save(commit=False)
        report.username = request.user.get_username()
        messages.success(request, "Raportul a fost creat!")
        user = request.user
        user.reports += 1
        user.save()
        report.save()
    else:
        messages.error(request, "Raportul nu a fost creat!")
    return HttpResponseRedirect(reverse('profile'))

def updateReport(request, report_id):
    form = reportForm(request.POST, instance= get_object_or_404(Report, pk=report_id))
    form.username = request.user.get_username()
    if (form.is_valid()):
        messages.success(request, "Raportul a fost editat!")
        user = form.save(commit=False)
        user.save()
    else:
        messages.error(request, "Raportul nu a fost editat")
    return HttpResponseRedirect(reverse('profile'))

def createReport(request):
    report = reportForm()
    context = {
            'report' : report,
            'path' : 'saveReport',
    }
    return render(request, 'editReport.html', context)

def viewReport(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, 'viewReport.html', {'report': report})


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

def editReport(request, report_id):
    object = get_object_or_404(Report, pk=report_id)
    report = reportForm(instance=object)
    if (request.user.username != object.username):
        # message user can't acces it
        return viewReport(request, report_id)
    context = {
        'report' : report,
        'path' : "updateReport" ,
    }
    return render(request, 'editReport.html', context)
