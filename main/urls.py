from django.urls import path

from main.views import (
    show_main, 
    show_experience, 
    show_projects, 
    show_discography, 
    create_project, 
    get_projects_json,
    delete_project,
    create_experience,
    get_experience_json,
    delete_experience,
    create_discography,
    get_discography_json,
    delete_discography,
    update_project,
    update_experience
)
app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("project/", show_projects, name="show_projects"),
    path("discography/", show_discography, name="show_discography"),
    path("project/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("project/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("project/<uuid:project_id>/edit/",update_project,name="edit_project"),
    path("experience/add/", create_experience, name="create_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("experience/<uuid:experience_id>/edit/",update_experience,name="edit_experience"),
    path("discography/add/", create_discography, name="create_discography"),
    path("api/discography/", get_discography_json, name="get_discography_json"),
    path("discography/<uuid:music_id>/delete/",delete_discography,name="delete_discography"),
    path("discography/<uuid:music_id>/edit/",update_experience,name="edit_discography"),
]