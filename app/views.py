from django.shortcuts import render
from .models import Bacteria, Gallery, Member, Phage, ResearchProject, TextContent

def index(request):
    ongoing_count = ResearchProject.objects.filter(status='ongoing').count()
    published_count = ResearchProject.objects.filter(status='published').count()
    total_count = ongoing_count + published_count
    about_us = TextContent.objects.get(id=1)
    ongooing = TextContent.objects.get(id=2)
    publication = TextContent.objects.get(id=3)

    context = {
        'ongoing_count': ongoing_count,
        'published_count': published_count,
        'total_count': total_count,
        'about_us': about_us.description,
        'ongoing': ongooing.description,
        'publication': publication.description,
    }
    return render(request, 'index.html', context)

def ongoing_research(request):
    research_projects = ResearchProject.objects.filter(status='ongoing')
    context = {'research_projects': research_projects}
    return render(request, 'ongoing_research.html', context)

def published_research(request):
    research_projects = ResearchProject.objects.filter(status='published')
    context = {'research_projects': research_projects}
    return render(request, 'published_research.html', context)

def members(request):
    categories = {
        'Principla Investigators': Member.objects.filter(category='lab_investigator'),
        'Coinvestigators': Member.objects.filter(category='lab_investigator_co'),
        'MS (Thesis) Students': Member.objects.filter(category='ms_thesis_student'),
        'Undergraduate Students': Member.objects.filter(category='undergraduate_student'),
        'Alumni Members': Member.objects.filter(category='alumni'),
    }

    context = {
        'member_categories': categories,
        'total_members': Member.objects.count(),
    }
    return render(request, 'members.html', context)

def gallery_view(request):
    images = Gallery.objects.all()
    context = {'images': images}
    return render(request, 'gallery.html', context)

def database_view(request):
    context = {
        'bacteria_list': Bacteria.objects.all(),
        'phage_list': Phage.objects.all(),
    }
    return render(request, 'database.html', context)
