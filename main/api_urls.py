from django.urls import path
from main import api_views

app_name = "api"
urlpatterns = [
    path("projects/", api_views.project_list, name="project-list"),
    path("projects/<uuid:project_id>/", api_views.project_detail, name="project-detail"),
    path("projects/<uuid:project_id>/star/", api_views.project_star, name="project-star"),
    path("experiences/", api_views.experience_list, name="experience-list"),
    path("experiences/<uuid:experience_id>/", api_views.experience_detail, name="experience-detail"),
    path("experiences/<uuid:experience_id>/star/", api_views.experience_star, name="experience-star"),
    path("discography/", api_views.music_list, name="discography-list"),
    path("discography/<uuid:music_id>/", api_views.music_detail, name="discography-detail"),
    path("discography/<uuid:music_id>/star/", api_views.music_star, name="discography-star"),
]