from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from eventReport.forms import EventReportForm
from eventReport.models import EventReport
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q

# Create your views here.
@login_required
def viewEventReport(request, report_id):
    report = get_object_or_404(EventReport, pk=report_id)
    return render(request, 'viewEventReport.html', {'report' : report})

@login_required
def createEventReport(request):
    if request.method == 'POST':
        form = EventReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Raportul a fost creat!")
            user = request.user
            user.eventReports += 1
            user.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.error(request, "Raportul nu a fost creat!")
    else:
        form = EventReportForm(initial = {'username' : request.user.get_username()})
    context = {
        'form' : form,
        'path' : '',
    }
    return render(request, 'editEventReport.html', context)

@login_required
def updateEventReport(request, report_id):
    if request.method == 'POST':
        form = EventReportForm(request.POST)
        if form.is_valid():
            messages.success(request, "Raportul a fost editat!")
            report = form.save(commit=False)
            report.id = report_id
            report.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.error(request, "Raportul nu a fost editat")
    else:
        report = get_object_or_404(EventReport, pk = report_id)
        form = EventReportForm(instance=report)
        if report.username != request.user.get_username():
            messages.error(request, "Doar creatorul poate edita formularul")
            return viewEventReport(request, report_id)
    context = {
        'form' : form,
        'path' : str(report_id),
    }
    return render(request, 'editEventReport.html', context)

@login_required
def deleteEventReport(request, report_id):
    report = get_object_or_404(EventReport, pk = report_id)
    if report.username != request.user.get_username():
        messages.error(request, "Doar creatorul poate șterge formularul")
        return viewReport(request, report_id)
    else:
        user = request.user
        user.eventReports -= 1
        user.save()
        EventReport.objects.filter(id = report_id).delete()
        messages.success(request, "Raportul a fost șters!")
        return HttpResponseRedirect(reverse('profile'))

@login_required
def searchEventReports(request):
    search = request.GET.get('search')
    if (not search):
        search = ""
    reports = EventReport.objects.all()
    if (not reports):
        reports = ""
    context = {
        'reports':reports,
    }
    return render(request, 'searchEventReports.html', context)
