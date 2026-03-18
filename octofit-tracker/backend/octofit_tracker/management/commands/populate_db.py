from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team='marvel', is_active=True)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team='marvel', is_active=True)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='dc', is_active=True)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team='dc', is_active=True)

        # Create activities
        Activity.objects.create(user=tony, type='running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='swimming', duration=25, date=timezone.now().date())
        Activity.objects.create(user=clark, type='flying', duration=60, date=timezone.now().date())

        # Create workouts
        Workout.objects.create(name='Pushups', description='Upper body strength', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Core strength', suggested_for='dc')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
