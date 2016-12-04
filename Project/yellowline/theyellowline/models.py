from django.db import models

# Create your models here.
class Event(models.Model):
    def __str__(self):
        return self.event_name
    category=(('A','Art'),('F','Food'),('M','Music'),('S','Shopping'),('T','Theatre'))
    paid=(('P','Paid'),('F','Free'))
    event_name=models.CharField(max_length=200)
    event_date=models.DateTimeField('event date')
    event_category=models.CharField(max_length=20,choices=category,default='Null')
    event_website=models.CharField(max_length=200,blank=True)
    event_venue=models.CharField(max_length=200)
    event_paid=models.CharField(max_length=20,choices=paid,default="Null")

class PaidEvent(models.Model):
    def __str__(self):
        return self.event_bms
##    def limit_to_paid():
##        return {'event_paid':'Paid'}
    bms=models.ForeignKey(Event,on_delete=models.CASCADE)
    event_bms=models.CharField(max_length=200)
   
