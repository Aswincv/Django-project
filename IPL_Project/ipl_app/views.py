from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from ipl_app.models import Matches, Deliveries
from django.db.models import Count, Sum, F, FloatField
from django.db.models.functions import Cast
import json


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def home(request):
    return render(request, 'ipl/home.html')


@cache_page(CACHE_TTL)
def find_matches_played_per_year(request):
    context = {
        'matches_played_per_year': Matches.objects.values('season').annotate(no_of_matches=Count('id')),
        'title': 'matchesplayedperyear'
    }
    return render(request, 'ipl/matchesplayedperyear.html', context)


@cache_page(CACHE_TTL)
def find_matches_won_of_all_teams_over_all_the_years(request):
    context = {
        'matches_won_of_all_teams_over_all_the_years': Matches.objects.values('winner', 'season').exclude(result="\'no result\'").annotate(total=Count('winner')).order_by('season')
    }
    return render(request, 'ipl/matcheswonofallteamsoveralltheyears.html', context)


@cache_page(CACHE_TTL)
def find_extra_runs_conceded_per_team_2016(request):
    context = {
        'extra_runs_conceded_per_team_2016': Deliveries.objects.values('bowling_team').annotate(extra_runs=Sum('extra_runs')).filter(match_id__in=Matches.objects.values('id').filter(season='2016'))
    }
    return render(request, 'ipl/extrarunsconcededperteam.html', context)


@cache_page(CACHE_TTL)
def find_top_economical_bowlers_2015(request):
    context = {
        'top_economical_bowlers_2015': Deliveries.objects.values('bowler').annotate(total_runs_sum=Sum('total_runs')).annotate(sum_bye_runs = Sum('bye_runs')).annotate(total_balls=Count('ball')).annotate(noballs=Sum('noball_runs')).annotate(wideballs=Sum('wide_runs')).annotate(ecconomy=Cast((F('total_runs_sum')-F('sum_bye_runs'))*6/(F('total_balls')-F('noballs')-F('wideballs')), FloatField())).filter(match_id__season=2015).order_by('ecconomy')[:10],
        'title': 'topeconomicalbowlers2015'
    }
    return render(request, 'ipl/topeconomicalbowlers2015.html', context)


@cache_page(CACHE_TTL)
def find_top_runs_over_all_the_years(request):
    context = {
        'top_runs_over_all_the_years': Deliveries.objects.values('match_id__season', 'batsman').annotate(runs=Sum('batsman_runs')).order_by('-runs')[:10],
    }
    return render(request,'ipl/toprunsoveralltheyear.html', context)


@cache_page(CACHE_TTL)
def plot_matches_played_per_year(request):
    context_list = json.dumps({'data': list(Matches.objects.values('season').annotate(no_of_matches=Count('id')))})
    return render(request, 'ipl/plotmatchesplayedperyear.html', context={"data": context_list})


@cache_page(CACHE_TTL)
def plot_extra_runs_conceded_per_team_2016(request):
    context_list = json.dumps({'data': list(Deliveries.objects.values('bowling_team').annotate(extra_runs=Sum('extra_runs')).filter(match_id__in=Matches.objects.values('id').filter(season='2016')))})
    return render(request, 'ipl/plotextrarunsconcededperteam.html', context={"data": context_list})


@cache_page(CACHE_TTL)
def plot_top_economical_bowlers_2015(request):
    context_list = json.dumps({'data': list(Deliveries.objects.values('bowler').annotate(total_runs_sum=Sum('total_runs')).annotate(sum_bye_runs = Sum('bye_runs')).annotate(total_balls=Count('ball')).annotate(noballs=Sum('noball_runs')).annotate(wideballs=Sum('wide_runs')).annotate(ecconomy=Cast((F('total_runs_sum')-F('sum_bye_runs'))*6/(F('total_balls')-F('noballs')-F('wideballs')), FloatField())).filter(match_id__season=2015).order_by('ecconomy')[:10])})
    return render(request, 'ipl/plottopecconomicalbowler.html', context={"data": context_list})


@cache_page(CACHE_TTL)
def plot_top_runs_over_all_the_years(request):
    context_list = json.dumps({'data': list(Deliveries.objects.values('match_id__season', 'batsman').annotate(runs=Sum('batsman_runs')).order_by('-runs')[:10])})
    return render(request, 'ipl/plottoprunsoveralltheyear.html', context={"data": context_list})


@cache_page(CACHE_TTL)
def plot_matches_won_of_all_teams_over_all_the_years(request):
    context_list = json.dumps({'data': list(Matches.objects.values('winner', 'season').exclude(result="\'no result\'").annotate(total=Count('winner')).order_by('season'))})
    return render(request, 'ipl/plotmatcheswonofallteamsoveralltheyears.html', context={"data": context_list})
