from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Project, Music
from main.forms import ProjectForm, ExperienceForm, DiscographyForm
# Create your views here.

def show_main(request):
    context = {
        "name": "Justin Lie",
        "npm": "2506591961",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A sophomore CS student at Universitas Indonesia, currently an active teaching assistant in Introduction to Digital Systems (IDS). "
            "Passionate in Game Design & Security."
        ),
    }
    return render(request, "index.html", context)

# Discography Views
def show_discography(request):
    json_response = get_discography_json(request)
    musics = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    musics = [music.object for music in musics]
    title_query = request.GET.get("title", "").strip()
        
    context = {
        "name": "Justin Lie",
        "discography_list": musics,
        "title_query": title_query,
    }
    return render(request, "discography.html", context)

def create_discography(request):
    form = DiscographyForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Lagu baru berhasil ditambahkan!")
        return redirect("main:show_discography")

    context = {
        "name": "Justin Lie",
        "form": form,
    }
    return render(request, "discography_form.html", context)

def get_discography_json(request):
    title_query = request.GET.get("title", "").strip()
    music_list = Music.objects.all()

    if title_query:
        music_list = music_list.filter(title__icontains=title_query)

    music_json = serializers.serialize("json", music_list)
    return HttpResponse(music_json, content_type="application/json")

def delete_discography(request, music_id):
    music = get_object_or_404(Music, pk=music_id)

    if request.method == "POST":
        music.delete()
        messages.success(request, "Lagu berhasil dihapus!")
        return redirect("main:show_discography")

    return redirect("main:show_discography")

def update_discography(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    form = DiscographyForm(request.POST or None, instance=music)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Lagu berhasil diperbarui!")
        return redirect("main:show_discography")

    context = {
        "name": "Justin Lie",
        "form": form,
        "music": music,
    }
    return render(request, "discography_form.html", context)

# Experience Views
def show_experience(request):
    json_response = get_experience_json(request)
    
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Justin Lie",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Justin Lie",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Justin Lie",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)

# Project Views
def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Justin Lie",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Justin Lie",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diperbarui!")
        return redirect("main:show_projects")

    context = {
        "name": "Justin Lie",
        "form": form,
        "project": project,
    }
    return render(request, "projects_form.html", context)