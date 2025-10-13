from django.http import HttpResponse
from django.shortcuts import render

from league_seasons.models import LeagueSeason


def about(request):
    return HttpResponse("This is a project developed by Eldred Brown.")


def welcome(request):
    return render(request, "website/welcome.html",
                  {"league_seasons": LeagueSeason.objects.all()})
