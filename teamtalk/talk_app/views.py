from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from talk_app import views
from .models import Player, Team, Coach
from .forms import TeamForm
from .serializers import TeamSerializer, PlayerSerializer, CoachSerializer


class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayersViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class CoachesViewSet(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


def index(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, "talk_app/index.html", context)


def register(request):
    if request.method == 'POST':
        team_form = TeamForm(request.POST)
        if team_form.is_valid():
            new_team = team_form.save()
            return HttpResponseRedirect("talk_app/index.html")
        else:
            print(team_form.errors)
    else:
        team_form = TeamForm()

    context = {'team_form': team_form}
    return render(request, "talk_app/register.html", context)
