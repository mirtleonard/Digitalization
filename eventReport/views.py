from django.core.files.storage import default_storage as storage
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from eventReport.filters import EventReportFilter
from eventReport.forms import EventReportForm
from eventReport.models import EventReport
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from googleAPI.api import *
from io import BytesIO
import os, zipfile

# Create your views here.

@login_required
def viewEventReport(request, report_id):
    report = get_object_or_404(EventReport, pk=report_id)
    try:
        photos = os.listdir(os.path.join(settings.MEDIA_ROOT, 'event' + str(report_id)))
    except OSError as e:
        downloadFiles('event' + str(report_id))
        try:
            photos = os.listdir(os.path.join(settings.MEDIA_ROOT, 'event' + str(report_id)))
        except:
            photos = ''
    path = settings.MEDIA_URL + 'event' + str(report_id) + '/'
    context = {
        'report' : report,
        'photos' : photos,
        'path' : path,
    }
    return render(request, 'viewEventReport.html', context)

@login_required
def createEventReport(request):
    if request.method == 'POST':
        form = EventReportForm(request.POST, request.FILES or None)
        photos = request.FILES.getlist('photos')
        if form.is_valid():
            report = form.save()
            saveFiles(photos, 'event' + str(report.id))
            messages.success(request, "Raportul a fost creat!")
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.error(request, "Raportul nu a fost creat!")
    else:
        form = EventReportForm(initial = {'username' : request.user.get_username()})
    context = {
        'form' : form,
    }
    return render(request, 'editEventReport.html', context)

@login_required
def updateEventReport(request, report_id):
    if request.method == 'POST':
        form = EventReportForm(request.POST)
        photos = request.FILES.getlist('photos')
        if form.is_valid():
            saveFiles(photos, 'event' + str(report_id))
            clearStorage('/event' + str(report_id))
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
    }
    return render(request, 'editEventReport.html', context)

@login_required
def deleteEventReport(request, report_id):
    report = get_object_or_404(EventReport, pk = report_id)
    if report.username != request.user.get_username():
        messages.error(request, "Doar creatorul poate ??terge formularul")
        return viewEventReport(request, report_id)
    else:
        deleteFile('event' + str(report_id))
        EventReport.objects.filter(id = report_id).delete()
        messages.success(request, "Raportul a fost ??ters!")
        return HttpResponseRedirect(reverse('profile'))

@login_required
def searchEventReports(request):
    reports = EventReportFilter(request.GET)
    context = {
        'reports':reports,
    }
    return render(request, 'searchEventReports.html', context)

@login_required
def download(request, report_id):
    path = os.path.join(settings.MEDIA_ROOT, 'event' + str(report_id))
    photos = os.listdir(path)
    zip_files = "%s.zip" % "img"

    bytesIO = BytesIO()

    zip = zipfile.ZipFile(bytesIO, 'w')

    for photo in photos:
        fpath = path + '/' + photo
        print(fpath)
        zip.write(fpath, photo)

    zip.close()
    response = HttpResponse(bytesIO.getvalue(), content_type="aplication/x-zip-compressed")
    response['Content-Disposition'] = 'attachement; filename=img.zip'
    return response
