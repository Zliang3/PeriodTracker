from django.db import models


class Events(models.Model):
    tasks = models.CharField(max_length=1000)
    calendar_date = models.DateField(null=True)


