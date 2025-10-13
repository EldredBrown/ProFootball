from django.contrib import admin

from league_seasons.models import League, Season, LeagueSeason

admin.site.register(League)
admin.site.register(Season)
admin.site.register(LeagueSeason)
