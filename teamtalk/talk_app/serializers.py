from rest_framework import serializers

from .models import Team, Player, Coach

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'coach', 'city', 'created_at')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'age', 'position', 'team')


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ('name', 'age', 'coaching_style')
