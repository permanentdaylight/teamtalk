from django.db import models
from django.contrib.auth.models import User

POSITIONS = (
    ('PG', 'Point Guard'),
    ('SG', 'Shooting Guard'),
    ('SF', 'Small Forward'),
    ('PF', 'Power Forward'),
    ('C', 'Center'),
)

COACHING_STYLE = (
    ('Off', 'Offensive'),
    ('Def', 'Defensive'),
    ('Bal', 'Balanced'),
)


class Team(models.Model):
    name = models.CharField(max_length=255)
    coach = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    position = models.CharField(choices=POSITIONS, max_length=3)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Coach(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    coaching_style = models.CharField(choices=COACHING_STYLE, max_length=1)

    class Meta:
        verbose_name_plural = "coaches"

    def __str__(self):
        return self.name
