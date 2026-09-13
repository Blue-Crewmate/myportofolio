from django.shortcuts import render
from main.models import Experience, Project, Music
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

def show_discography(request):
    context = {
        "name": "Justin Lie",
        "music_list": Music.objects.all(),
        }
    return render(request, "discography.html", context)

def show_experience(request):
    context = {
        "name": "Justin Lie",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_project(request):
    context = {
        "name": "Justin Lie",
        "project_list": Project.objects.all(),
    }
    return render(request, "project.html", context)
