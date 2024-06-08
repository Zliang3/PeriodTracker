from django.db import models


class Events(models.Model):
    tasks = models.CharField(max_length=1000)
    calendar_date = models.DateField(null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()



