from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User



class Users(models.Model):
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=150)
    class Meta:
        ordering = ('real_name',)

    def __str__(self):
        return (self.real_name)
    
class ActivityPeriod(models.Model):
	user = models.ForeignKey(Users,related_name='activity_periods',on_delete  = models.CASCADE)
	start_time = models.DateTimeField(default = timezone.now)
	end_time   = models.DateTimeField(default = timezone.now) 