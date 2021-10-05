from rest_framework import serializers
from .models import locationDetails

class locationSerializer(serializers.ModelSerializer):
	class Meta:
		model = locationDetails
		fields = '__all__'
