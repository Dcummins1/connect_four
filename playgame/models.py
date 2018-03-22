from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

#User.objects.get(username=the_username).pk
class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    player_1 = models.IntegerField()
    player_2 = models.IntegerField(null=True)
    won = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    moves =  models.CharField(max_length=255, null=True)

    @property
    def user_2(self):
        return User.objects.get(pk=self.player_2)

    @property
    def user_1(self):
        return User.objects.get(pk=self.player_1)

    def __str__(self):
        return str(self.game_id)
