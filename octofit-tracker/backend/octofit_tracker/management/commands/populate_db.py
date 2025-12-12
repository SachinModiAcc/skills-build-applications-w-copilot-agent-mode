from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Drop collections directly to avoid unhashable model instance errors
        from django.db import connection
        db = connection.cursor().db_conn.client['octofit_db']
        db['leaderboard'].drop()
        db['activities'].drop()
        db['workouts'].drop()
        db['users'].drop()
        db['teams'].drop()

        # Now repopulate as before
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        w1 = Workout.objects.create(name='Super Strength', description='Strength training for heroes', suggested_for='Marvel')
        w2 = Workout.objects.create(name='Flight Training', description='Aerial maneuvers', suggested_for='DC')

        Activity.objects.create(user=tony, type='Run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='Swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Martial Arts', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, type='Flight', duration=50, date=timezone.now().date())

        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=95)
        Leaderboard.objects.create(user=clark, score=98)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength training for heroes', suggested_for='Marvel')
        w2 = Workout.objects.create(name='Flight Training', description='Aerial maneuvers', suggested_for='DC')

        # Create activities
        Activity.objects.create(user=tony, type='Run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='Swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Martial Arts', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, type='Flight', duration=50, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=95)
        Leaderboard.objects.create(user=clark, score=98)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
