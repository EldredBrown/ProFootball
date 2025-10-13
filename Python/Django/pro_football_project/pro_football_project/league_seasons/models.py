from django.db import models


class Season(models.Model):
    year = models.IntegerField()
    weeks_scheduled = models.IntegerField(default=0)
    weeks_completed = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.year}"


class League(models.Model):
    long_name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=5)
    first_season_year = models.IntegerField()
    last_season_year = models.IntegerField()

    def __str__(self):
        return f"{self.long_name} ({self.short_name})"


class LeagueSeason(models.Model):
    league_name = models.ForeignKey(League, on_delete=models.CASCADE)
    season_year = models.ForeignKey(Season, on_delete=models.CASCADE)
    total_games = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    average_points = models.DecimalField(max_digits=16, decimal_places=14, default=0)

    def __str__(self):
        return f"{self.league_name} : {self.season_year}"
