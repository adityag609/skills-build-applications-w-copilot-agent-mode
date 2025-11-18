from rest_framework import routers
from octofit_tracker import viewsets
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewSet)
router.register(r'teams', viewsets.TeamViewSet)
router.register(r'activities', viewsets.ActivityViewSet)
router.register(r'workouts', viewsets.WorkoutViewSet)
router.register(r'leaderboard', viewsets.LeaderboardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
