from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from report.models import Report
from django.urls import reverse
from django.db.models import Q

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

def searchReport(request):
    search = request.GET.get('search')
    print(search)
    reports = Report.objects.filter(Q(title__icontains = search) |
                                    Q(username__icontains = search) |
                                    Q(branch__icontains = search) |
                                    Q(date__icontains = search) |
                                    Q(description__icontains = search) |
                                    Q(goals__icontains = search) |
                                    Q(strengths__icontains = search) |
                                    Q(weaknesses__icontains = search) |
                                    Q(goals__icontains = search) |
                                    Q(duration__icontains = search) |
                                    Q(areas__icontains = search) |
                                    Q(improvements__icontains = search))
    if (not reports):
        reports = ""
    context = {'reports' : reports}
    return render(request, 'ViewReports.html', context)
