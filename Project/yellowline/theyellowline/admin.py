from django.contrib import admin

# Register your models here.
from .models import Event,PaidEvent

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['event_name']}),
        ('Date information', {'fields': ['event_date']}),
        ('Venue',{'fields':['event_venue']}),
        ('Category',{'fields':['event_category']}),
        ('Webpage',{'fields':['event_website']}),
        ('Paid Event',{'fields':['event_paid'], 'classes': ['collapse']})
        
    ]


admin.site.register(Event,EventAdmin)
admin.site.register(PaidEvent)
