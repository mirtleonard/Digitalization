from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from report.models import Report
from django.urls import reverse

# Create your views here.

def submitReport(request):
    report = Report(
        username = request.user.get_username(),
        location = request.POST.get('location'),
        branch = request.POST.get('branch'),
        areas = request.POST.get('areas'),
        title = request.POST.get('title'),
        duration = request.POST.get('duration'),
        date = request.POST.get('date'),
        participants = request.POST.get('participants'),
        description = request.POST.get('description'),
        goals = request.POST.get('goals'),
        strengths = request.POST.get('strengths'),
        weaknesses = request.POST.get('weaknesses'),
        improvements = request.POST.get('improvements'),
    )
    report.save()
    user = request.user
    user.reports += 1
    user.save()
    return HttpResponseRedirect(reverse('profile'))

def addReport(request):
    return render(request, 'AddReport.html')

def viewReports(request):
    reports = Report.objects.order_by('date')
    context = {'reports' : reports}
    return render(request, 'ViewReports.html', context)
