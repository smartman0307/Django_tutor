from django.urls import path
from . import views

urlpatterns = [
    path("", views.Project_index, name="project_index"),
    path("<int:pk>/", views.Project_detail, name="project_detail"),
]
