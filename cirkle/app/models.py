from django.db import models


class Cirkle(models.Model):
    class Colors(models.TextChoices):
        BLACK = 'black', 'Black'
        RED = 'red', 'Red'
        GREEN = 'green', 'Green'
        BLUE = 'blue', 'Blue'

    radius = models.IntegerField()

    @property
    def width(self):
        return self.radius * 2

    @property
    def height(self):
        return self.radius * 2

    color = models.CharField(
        max_length=255,
        choices=Colors.choices,
        default=Colors.BLACK
    )
