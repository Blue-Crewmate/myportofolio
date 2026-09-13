from django.urls import path

from main.views import show_main, show_experience, show_project, show_discography

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("project/", show_project, name="show_project"),
    path("discography/", show_discography, name="show_discography")
]