from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView

from league_seasons.models import LeagueSeason, League, Season


@cache_page(15*60)
def detail(request, id):
    league_season = get_object_or_404(LeagueSeason, pk=id)
    return render(request, "league_seasons/detail.html", {"league_season": league_season})


class LeaguesView(ListView):
    template_name = "league_seasons/leagues_list.html"
    queryset = League.objects.all()
    context_object_name = "leagues"


class SeasonsView(ListView):
    template_name = "league_seasons/seasons_list.html"
    queryset = Season.objects.all()
    # queryset = [s for s in range(1920, 2024)]
    context_object_name = "seasons"
    paginate_by = 25


LeagueSeasonForm = modelform_factory(LeagueSeason, exclude=[])


@require_http_methods(["GET", "POST"])
def new(request):
    if request.method == "POST":
        form = LeagueSeasonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = LeagueSeasonForm()

    return render(request, "league_seasons/new.html", {"form": form})
