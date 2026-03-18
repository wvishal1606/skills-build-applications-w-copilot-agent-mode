from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='dc', is_active=True)
        self.assertEqual(user.name, 'Bruce Wayne')
        self.assertEqual(user.team, 'dc')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='marvel', description='Marvel superheroes')
        self.assertEqual(team.name, 'marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(name='Clark Kent', email='clark@dc.com', team='dc', is_active=True)
        activity = Activity.objects.create(user=user, type='running', duration=30, date='2026-03-18')
        self.assertEqual(activity.type, 'running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='dc', description='DC superheroes')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body', suggested_for='marvel')
        self.assertEqual(workout.name, 'Pushups')
