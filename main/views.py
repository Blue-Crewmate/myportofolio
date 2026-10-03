from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.utils.http import url_has_allowed_host_and_scheme
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied

from main.models import Experience, Project, Music
from main.forms import ProjectForm, ExperienceForm, DiscographyForm
import datetime
# Create your views here.

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Justin Lie",
        "npm": "2506591961",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A sophomore CS student at Universitas Indonesia, currently an active teaching assistant in Introduction to Digital Systems (IDS). "
            "Passionate in Game Design & Security."
        ),
        "last_login": last_login,
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
        "is_editor": request.user.groups.filter(name='Editor').exists(),
    }
    return render(request, "discography.html", context)

@login_required(login_url="/login/")
def create_discography(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

    music_json = serializers.serialize(
        "json", music_list, use_natural_foreign_keys=True
    )
    return HttpResponse(music_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_discography(request, music_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    music = get_object_or_404(Music, pk=music_id)

    if request.method == "POST":
        music.delete()
        messages.success(request, "Lagu berhasil dihapus!")
        return redirect("main:show_discography")

    return redirect("main:show_discography")

@login_required(login_url="/login/")
def update_discography(request, music_id):
    if not (request.user.is_superuser or request.user.groups.filter(name='Editor').exists()):
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def toggle_star_discography(request, music_id):
    music = get_object_or_404(Music, pk=music_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in music.starred_by.all():
            music.starred_by.remove(request.user)
        else:
            music.starred_by.add(request.user)

    return redirect("main:show_discography")


# Experience Views
def show_experience(request):
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Justin Lie",
        "title_query": title_query,
        "is_editor": request.user.groups.filter(name='Editor').exists(),
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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
    experiences = Experience.objects.prefetch_related("starred_by").all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    # Construct JSON data manually to include starred_by logic
    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([user.username for user in starred_users])

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "thumbnail": experience.thumbnail,
                "started_at": experience.started_at,
                "ended_at": experience.ended_at,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not (request.user.is_superuser or request.user.groups.filter(name='Editor').exists()):
        raise PermissionDenied

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

@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser(): 
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(experience.id)},
            status=201
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

# Project Views
def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Justin Lie",
        "title_query": title_query,
        "is_editor": request.user.groups.filter(name='Editor').exists(),
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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
    projects = Project.objects.prefetch_related("starred_by").all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Construct JSON data manually to include starred_by logic
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([user.username for user in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "collaborators": project.collaborators,
                "status": project.status,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def update_project(request, project_id):
    if not (request.user.is_superuser or request.user.groups.filter(name='Editor').exists()):
        raise PermissionDenied

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

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


# Authentication 
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Justin Lie",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    # Gets the redirect URL from /?next=
    if request.GET.get("next"):
        request.session["login_next"] = request.GET["next"]

    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)

        next_url = request.session.get("login_next")
        # url_has_allowed_host_and_scheme is used to check whether the next_url is safe to redirect
        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure(),
        ):
            response = redirect(next_url)
        else:
            response = redirect("main:show_main")


        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Justin Lie",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response