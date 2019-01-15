from django.core.management.base import BaseCommand, CommandError
from ipl_app.models import Matches, Deliveries
from django.db import connection
import csv
from django.db import transaction
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'write data from csv file to mysql database'

    def handle(self, *args, **options):
        flag = True
        match_list = []
        csv_file = "/home/aswincv/djangoProjects/IPL/ipl_app/static/matches.csv"
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if flag:
                    flag = False
                    continue
                else:
                    match_object = Matches()
                    match_object.id = row[0]
                    match_object.season = row[1]
                    match_object.city = row[2]
                    match_object.date = row[3]
                    match_object.team1 = row[4]
                    match_object.team2 = row[5]
                    match_object.toss_winner = [6]
                    match_object.toss_decision = row[7]
                    match_object.result = row[8]
                    match_object.dl_applied = row[9]
                    match_object.winner = row[10]
                    match_object.win_by_runs = row[11]
                    match_object.win_by_wickets = row[12]
                    match_object.player_of_match = row[13]
                    match_object.venue = row[14]
                    match_object.umpire1 = row[15]
                    match_object.umpire2 = row[16]
                    match_object.umpire3 = row[17]
                match_list.append(match_object)
        with transaction.atomic():
            Matches.objects.bulk_create(match_list)
    flag = True
    delivery_object_list = []
    csv_file = "/home/aswincv/djangoProjects/IPL/ipl_app/static/deliveries.csv"
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if flag:
                flag = False
                continue
            else:
                delivery_object = Deliveries()
                delivery_object.match_id = row[0]
                delivery_object.inning = row[1]
                delivery_object.batting_team = row[2]
                delivery_object.bowling_team = row[3]
                delivery_object.over = row[4]
                delivery_object.ball = row[5]
                delivery_object.batsman = row[6]
                delivery_object.non_striker = row[7]
                delivery_object.bowler = row[8]
                delivery_object.is_super_over = row[9]
                delivery_object.wide_runs = row[10]
                delivery_object.bye_runs = row[11]
                delivery_object.legbye_runs = row[12]
                delivery_object.noball_runs = row[13]
                delivery_object.penalty_runs = row[14]
                delivery_object.batsman_runs = row[15]
                delivery_object.extra_runs = row[16]
                delivery_object.otal_runs = row[17]
                delivery_object.player_dismissed = row[18]
                delivery_object.dismissal_kind = row[19]
                delivery_object.fielder = row[20]
            delivery_object_list.append(delivery_object)
    # with transaction.atomic():
    # try:
        # with transaction.atomic():
    Deliveries.objects.bulk_create(delivery_object_list)
    # except SomeError:
        # handle_exception()

            # Matches.objects.bulk_create(match_list)
