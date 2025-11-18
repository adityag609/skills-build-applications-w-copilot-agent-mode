from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Captain America', email='cap@marvel.com', team=marvel),
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Batman', email='batman@dc.com', team=dc),
            User(name='Superman', email='superman@dc.com', team=dc),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create workouts
        workouts = [
            Workout(name='Cardio Blast', description='High intensity cardio', difficulty='Hard'),
            Workout(name='Strength Training', description='Build muscle', difficulty='Medium'),
            Workout(name='Yoga Flow', description='Flexibility and balance', difficulty='Easy'),
        ]
        for workout in workouts:
            workout.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30)
        Activity.objects.create(user=users[1], type='Cycling', duration=45)
        Activity.objects.create(user=users[2], type='Swimming', duration=60)
        Activity.objects.create(user=users[3], type='Martial Arts', duration=50)
        Activity.objects.create(user=users[4], type='Weightlifting', duration=40)
        Activity.objects.create(user=users[5], type='Yoga', duration=35)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=120)
        Leaderboard.objects.create(team=dc, points=110)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
