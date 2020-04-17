from django.urls import path
from . import views


urlpatterns = [
    path ('', views.homepage),
    path ('blog/', views.blog),
    path ('bio/', views.bio),
    path ('contact/', views.contact),
    path ('project/', views.projects),
]
