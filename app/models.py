from django.db import models


class Kube(models.Model):
    class Colors(models.TextChoices):
        BLACK = 'black', 'Black'
        RED = 'red', 'Red'
        GREEN = 'green', 'Green'
        BLUE = 'blue', 'Blue'

    width = models.IntegerField()
    height = models.IntegerField()

    color = models.CharField(
        max_length=255,
        choices=Colors.choices,
        default=Colors.BLACK
    )
