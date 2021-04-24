from django.db import models


class Law(models.Model):
    name = models.CharField(max_length=20)


class Player(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.name
