from django.db import models


class Timeu(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    project = models.CharField(max_length=200)
    date = models.DateTimeField()
    
    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'timer'
