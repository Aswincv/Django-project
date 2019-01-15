from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="ipl-home"),
    path('matchesplayedperyear/', views.find_matches_played_per_year, name="ipl-matchesplayedperyear"),
    path('matcheswonofallteamsoveralltheyears/', views.find_matches_won_of_all_teams_over_all_the_years, name="ipl-matcheswonofallteamsoveralltheyears"),
    path('extrarunsconcededperteam/', views.find_extra_runs_conceded_per_team_2016, name="ipl-extrarunsconcededperteam"),
    path('topeconomicalbowlers/', views.find_top_economical_bowlers_2015, name="ipl-topeconomicalbowlers"),
    path('performanceofplayers/', views.find_top_runs_over_all_the_years, name='ipl-toprunsoveralltheyear'),
    path('plotmatchesplayedperyear/', views.plot_matches_played_per_year, name="ipl-plotmatchesplayedperyear"),
    path('plotmatcheswonofallteamsoveralltheyears/', views.plot_matches_won_of_all_teams_over_all_the_years, name="ipl-plotmatcheswonofallteamsoveralltheyears"),
    path('plotextrarunsconcededperteam/', views.plot_extra_runs_conceded_per_team_2016, name="ipl-plotextrarunsconcededperteam"),
    path('plottopeconomicalbowler/', views.plot_top_economical_bowlers_2015, name="ipl-plottopeconomicalbowler"),
    path('plot-performanceofplayers/', views.plot_top_runs_over_all_the_years, name='ipl-plottoprunsoveralltheyear'),
]
