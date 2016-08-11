from django import forms
from django.contrib.auth.models import User
from .models import Team, Player, Coach

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'coach', 'city', 'photo')

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('name', 'age', 'position', 'team')

class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ('name', 'age', 'coaching_style')
