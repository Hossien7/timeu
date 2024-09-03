from django.db import models


class Timeu(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    project = models.CharField(max_length=200)
    date = models.DateTimeField()

    def get_duration(self):
        duration = self.end_time - self.start_time
        return duration
    
    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'timer'
