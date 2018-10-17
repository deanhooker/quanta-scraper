"""Defines URL patterns for scraper."""

from django.urls import path

from . import views

app_name = 'scraper'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    # Scrape articles.
    path('scrape/', views.scrape, name='scrape'),
]