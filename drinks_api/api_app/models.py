from django.db import models

class Drink(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return f"{self.name}"