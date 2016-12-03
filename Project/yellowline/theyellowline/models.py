from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_datetime = models.DateTimeField('date and time of event')
    event_time = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)