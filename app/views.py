from django.shortcuts import get_object_or_404, render
from .models import Bacteria, Gallery, Member, Phage, ResearchProject, TextContent

def index(request):
    ongoing_count = ResearchProject.objects.filter(status='ongoing').count()
    published_count = ResearchProject.objects.filter(status='published').count()
    total_count = ongoing_count + published_count
    about_us = TextContent.objects.get(id=1)
    ongooing = TextContent.objects.get(id=2)
    publication = TextContent.objects.get(id=3)
    slider_images = Gallery.objects.filter(slider_image=True).order_by('-uploaded_at')[:5]

    context = {
        'ongoing_count': ongoing_count,
        'published_count': published_count,
        'total_count': total_count,
        'about_us': about_us.description,
        'ongoing': ongooing.description,
        'publication': publication.description,
        'slider_images': slider_images,
    }
    return render(request, 'index.html', context)

def ongoing_research(request):
    research_projects = ResearchProject.objects.filter(status='ongoing').order_by('-date')
    context = {'research_projects': research_projects}
    return render(request, 'ongoing_research.html', context)

def published_research(request):
    research_projects = ResearchProject.objects.filter(status='published').order_by('-date')
    context = {'research_projects': research_projects}
    return render(request, 'published_research.html', context)

def members(request):
    categories = {
        'Principal Investigators': Member.objects.filter(category='lab_investigator'),
        'Coinvestigators': Member.objects.filter(category='lab_investigator_co'),
        'PhD Students': Member.objects.filter(category='phd_student'),
        'MS (Thesis) Students': Member.objects.filter(category='ms_thesis_student'),
        'Undergraduate Students': Member.objects.filter(category='undergraduate_student'),
        'Alumni Members': Member.objects.filter(category='alumni'),
    }

    context = {
        'member_categories': categories,
        'total_members': Member.objects.count(),
    }
    return render(request, 'members.html', context)


def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if member.biography:
        member.biography = member.biography.strip()

    educations = member.educations.all().order_by('position')
    research_interests = member.research_interests.all().order_by('position')
    active_projects = member.active_research_projects.all().order_by('position')
    prev_projects = member.prev_research_projects.all().order_by('position')
    total_projects_count = active_projects.count() + prev_projects.count()
    affiliations = member.external_affiliations.all().order_by('position')
    awards = member.awards.all().order_by('-year')
    publications = member.publications.all().order_by('-year')
    teachings = member.teachings.all().order_by('position')
    conferences = member.conferences.all().order_by('-year')

    context = {
        'member': member,
        'educations': educations,
        'research_interests': research_interests,
        'active_projects': active_projects,
        'prev_projects': prev_projects,
        'affiliations': affiliations,
        'awards': awards,
        'publications': publications,
        'teachings': teachings,
        'conferences': conferences,
        'total_projects_count': total_projects_count,
    }

    return render(request, 'member_detail.html', context)


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


