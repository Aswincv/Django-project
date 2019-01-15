from django.shortcuts import render
from ipl_app.models import Matches, Deliveries
from django.db.models import Count, Sum, F, FloatField
from django.db.models.functions import Cast
import json

matches_played_per_year = Matches.objects.values('season').annotate(no_of_matches=Count('id'))
matches_won_of_all_teams_over_all_the_years = Matches.objects.values('winner', 'season').exclude(result="\'no result\'").annotate(total=Count('winner')).order_by('season')
extra_runs_conceded_per_team_2016 = Deliveries.objects.values('bowling_team').annotate(extra_runs=Sum('extra_runs')).filter(match_id__in=Matches.objects.values('id').filter(season='2016'))
top_economical_bowlers_2015 = Deliveries.objects.values('bowler').annotate(total_runs_sum=Sum('total_runs')).annotate(sum_bye_runs = Sum('bye_runs')).annotate(total_balls=Count('ball')).annotate(noballs=Sum('noball_runs')).annotate(wideballs=Sum('wide_runs')).annotate(ecconomy=Cast((F('total_runs_sum')-F('sum_bye_runs'))*6/(F('total_balls')-F('noballs')-F('wideballs')), FloatField())).filter(match_id__season=2015).order_by('ecconomy')[:10]
top_runs_over_all_the_years = Deliveries.objects.values('match_id__season', 'batsman').annotate(runs=Sum('batsman_runs')).order_by('-runs')[:10]


def home(request):
    return render(request, 'ipl/home.html')


def find_matches_played_per_year(request):
    context = {
        'matches_played_per_year': matches_played_per_year,
        'title': 'matchesplayedperyear'
    }
    return render(request, 'ipl/matchesplayedperyear.html', context)


def find_matches_won_of_all_teams_over_all_the_years(request):
    context = {
        'matches_won_of_all_teams_over_all_the_years': matches_won_of_all_teams_over_all_the_years
    }
    return render(request, 'ipl/matcheswonofallteamsoveralltheyears.html', context)


def find_extra_runs_conceded_per_team_2016(request):
    context = {
        'extra_runs_conceded_per_team_2016': extra_runs_conceded_per_team_2016,
        'title': 'extrarunsconcededperteam2016'
    }
    return render(request, 'ipl/extrarunsconcededperteam.html', context)


def find_top_economical_bowlers_2015(request):
    context = {
        'top_economical_bowlers_2015': top_economical_bowlers_2015,
        'title': 'topeconomicalbowlers2015'
    }
    return render(request, 'ipl/topeconomicalbowlers2015.html', context)


def find_top_runs_over_all_the_years(request):
    context = {
        'top_runs_over_all_the_years': top_runs_over_all_the_years,
    }
    return render(request,'ipl/toprunsoveralltheyear.html', context)


def plot_matches_played_per_year(request):
    context_list = json.dumps({'data': list(matches_played_per_year)})
    return render(request, 'ipl/plotmatchesplayedperyear.html', context={"data": context_list})


def plot_extra_runs_conceded_per_team_2016(request):
    context_list = json.dumps({'data': list(extra_runs_conceded_per_team_2016)})
    return render(request, 'ipl/plotextrarunsconcededperteam.html', context={"data": context_list})


def plot_top_economical_bowlers_2015(request):
    context_list = json.dumps({'data': list(top_economical_bowlers_2015)})
    return render(request, 'ipl/plottopecconomicalbowler.html', context={"data": context_list})


def plot_top_runs_over_all_the_years(request):
    context_list = json.dumps({'data': list(top_runs_over_all_the_years)})
    return render(request, 'ipl/plottoprunsoveralltheyear.html', context={"data": context_list})


def plot_matches_won_of_all_teams_over_all_the_years(request):
    context_list = json.dumps({'data': list(matches_won_of_all_teams_over_all_the_years)})
    return render(request, 'ipl/plotmatcheswonofallteamsoveralltheyears.html', context={"data": context_list})
