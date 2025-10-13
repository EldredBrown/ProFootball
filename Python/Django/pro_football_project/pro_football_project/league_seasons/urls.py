from django.urls import path

from . import views
from .views import LeaguesView, SeasonsView

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('leagues', LeaguesView.as_view(), name="leagues"),
    path('seasons', SeasonsView.as_view(), name="seasons"),
    path('new', views.new, name="new"),
]
