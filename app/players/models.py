from django.db import models


class Player(models.Model):
    epic_name = models.CharField(max_length=100, unique=True)
    epic_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.epic_name
