from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from report.models import Report
from django.urls import reverse
from django.db.models import Q

# Create your views here.

def submitReport(request):
    report = Report(
        username = request.user.get_username(),
        location = request.POST.get('location'),
        branch = request.POST.get('branch'),
        title = request.POST.get('title'),
        areas = request.POST.getlist('areas'),
        duration = request.POST.get('duration'),
        date = request.POST.get('date'),
        participants = request.POST.get('participants'),
        description = request.POST.get('description'),
        goals = request.POST.get('goals'),
        strengths = request.POST.get('strengths'),
        weaknesses = request.POST.get('weaknesses'),
        improvements = request.POST.get('improvements'),
    )
    print(report.areas)
    report.save()
    user = request.user
    user.reports += 1
    user.save()
    return HttpResponseRedirect(reverse('profile'))

def addReport(request):
    return render(request, 'addReport.html')

def viewReport(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, 'viewReport.html', {'report': report})


def searchReport(request):
    search = request.GET.get('search')
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
    for x in request.GET:
        print(x, request.GET.get(x))
    if (request.GET.get('areas') != ""):
        reports = reports.filter(areas__icontains = 'fizica')
    if (not reports):
        reports = ""
    context = {'reports' : reports}
    return render(request, 'searchReport.html', context)
