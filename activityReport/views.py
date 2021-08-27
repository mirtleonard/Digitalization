from django.core.files.storage import default_storage as storage
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from activityReport.filters import ActivityReportFilter
from django.shortcuts import render, get_object_or_404
from django.contrib.staticfiles.utils import get_files
from activityReport.forms import ActivityReportForm
from activityReport.models import ActivityReport
from django.core.files.base import ContentFile
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
import os, shutil, zipfile
from io import BytesIO

# Create your views here.
def saveActivityPhotos(photos, id):
    storage_path = os.path.join(settings.MEDIA_ROOT, 'activityReport/' + str(id) + '/img.png')
    for photo in photos:
        storage.save(storage_path, photo)

@login_required
def viewActivityReport(request, report_id):
    photos = ''
    try:
        photos = os.listdir(os.path.join(settings.MEDIA_ROOT, 'activityReport/' + str(report_id)))
    except OSError as e:
        photos = ''
    report = get_object_or_404(ActivityReport, pk=report_id)
    path = settings.MEDIA_URL + 'activityReport/' + str(report_id) + '/'
    context = {
        'report' : report,
        'photos' : photos,
        'path' : path,
    }
    return render(request, 'viewActivityReport.html', context)

@login_required
def createActivityReport(request):
    if request.method == 'POST':
        form = ActivityReportForm(request.POST, request.FILES or None)
        photos = request.FILES.getlist('photos')
        if form.is_valid():
            report = form.save()
            saveActivityPhotos(photos, report.id)
            messages.success(request, "Raportul a fost creat!")
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.error(request, "Raportul nu a fost creat!")
    else:
        form = ActivityReportForm(initial = {'username' : request.user.get_username()})
    context = {
        'report' : form,
    }
    return render(request, 'editActivityReport.html', context)

@login_required
def updateActivityReport(request, report_id):
    if request.method == 'POST':
        form = ActivityReportForm(request.POST, request.FILES or None)
        photos = request.FILES.getlist('photos')
        if form.is_valid():
            saveActivityPhotos(photos, report_id)
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
    }
    return render(request, 'editActivityReport.html', context)

@login_required
def deleteActivityReport(request, report_id):
    report = get_object_or_404(ActivityReport, pk = report_id)
    if report.username != request.user.get_username():
        messages.error(request, "Doar creatorul poate șterge formularul")
        return viewActivityReport(request, report_id)
    else:
        try:
            shutil.rmtree(settings.MEDIA_ROOT + '/activityReport/' + str(report_id))
        except OSError as e:
            pass
        ActivityReport.objects.filter(id = report_id).delete()
        messages.success(request, "Raportul a fost șters!")
        return HttpResponseRedirect(reverse('profile'))

@login_required
def searchActivityReports(request):
    reports = ActivityReportFilter(request.GET)
    context = {
        'reports': reports,
    }
    return render(request, 'searchActivityReports.html', context)

@login_required
def download(request, report_id):
    path = os.path.join(settings.MEDIA_ROOT, 'activityReport/' + str(report_id))
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
