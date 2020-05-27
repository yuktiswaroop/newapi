from rest_framework import serializers
from .models import Users,ActivityPeriod

class ASerializer(serializers.ModelSerializer):
	class Meta:
		model  = ActivityPeriod
		fields = ['start_time','end_time']
		 

class BSerializer(serializers.ModelSerializer):
	activity_periods = ASerializer(many = True,read_only=True)
	class Meta:
		model  = Users
		fields = ['real_name','tz','activity_periods']
