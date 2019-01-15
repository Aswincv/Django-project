from django.db import models


class Deliveries(models.Model):
    match = models.ForeignKey('Matches', models.DO_NOTHING, blank=True, null=True)
    inning = models.IntegerField(blank=True, null=True)
    batting_team = models.CharField(max_length=50, blank=True, null=True)
    bowling_team = models.CharField(max_length=50, blank=True, null=True)
    over_field = models.IntegerField(db_column='over_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ball = models.IntegerField(blank=True, null=True)
    batsman = models.CharField(max_length=50, blank=True, null=True)
    non_striker = models.CharField(max_length=50, blank=True, null=True)
    bowler = models.CharField(max_length=50, blank=True, null=True)
    is_super_over = models.IntegerField(blank=True, null=True)
    wide_runs = models.IntegerField(blank=True, null=True)
    bye_runs = models.IntegerField(blank=True, null=True)
    legbye_runs = models.IntegerField(blank=True, null=True)
    noball_runs = models.IntegerField(blank=True, null=True)
    penalty_runs = models.IntegerField(blank=True, null=True)
    batsman_runs = models.IntegerField(blank=True, null=True)
    extra_runs = models.IntegerField(blank=True, null=True)
    total_runs = models.IntegerField(blank=True, null=True)
    player_dismissed = models.CharField(max_length=5, blank=True, null=True)
    dismissal_kind = models.CharField(max_length=50, blank=True, null=True)
    fielder = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.match)

    class Meta:
        managed = False
        db_table = 'DELIVERIES'




class Matches(models.Model):
    id = models.IntegerField(primary_key=True)
    season = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=15, blank=True, null=True)
    team1 = models.CharField(max_length=50, blank=True, null=True)
    team2 = models.CharField(max_length=50, blank=True, null=True)
    toss_winner = models.CharField(max_length=50, blank=True, null=True)
    toss_decision = models.CharField(max_length=50, blank=True, null=True)
    result = models.CharField(max_length=50, blank=True, null=True)
    dl_applied = models.CharField(max_length=50, blank=True, null=True)
    winner = models.CharField(max_length=50, blank=True, null=True)
    win_by_runs = models.IntegerField(blank=True, null=True)
    win_by_wickets = models.IntegerField(blank=True, null=True)
    player_of_match = models.CharField(max_length=50, blank=True, null=True)
    venue = models.CharField(max_length=250, blank=True, null=True)
    umpire1 = models.CharField(max_length=50, blank=True, null=True)
    umpire2 = models.CharField(max_length=50, blank=True, null=True)
    umpire3 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.match)

    class Meta:
        managed = False
        db_table = 'MATCHES'

    # class User(AbstractUser):
    #     pass
