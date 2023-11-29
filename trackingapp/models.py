from django.db import models
from django.conf import settings

class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    category = models.CharField(max_length=50)
    amount = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.category


class Budget(models.Model):
    name = models.CharField(max_length=40)
    Amount = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name

