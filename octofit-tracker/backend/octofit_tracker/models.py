from djongo import models


class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name


class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, to_field='_id', related_name='members')
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='_id', related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'activities'
    def __str__(self):
        return f"{self.user.name} - {self.type}"


class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=50)
    class Meta:
        db_table = 'workouts'
    def __str__(self):
        return self.name


class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, to_field='_id', related_name='leaderboard')
    points = models.IntegerField(default=0)
    class Meta:
        db_table = 'leaderboard'
    def __str__(self):
        return f"{self.team.name} - {self.points}"
