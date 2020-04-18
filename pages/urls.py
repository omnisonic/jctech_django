from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, BlogPageView  #new
from pages import views


urlpatterns = [
    path ('about', AboutPageView.as_view(), name='about'),
    path ('blog', BlogPageView.as_view(), name='blog'),
    path ('projects', views.projects, name='projects'),
    path ('contact', ContactPageView.as_view(), name='contact'),
    path ('', HomePageView.as_view(), name='home'),

]
