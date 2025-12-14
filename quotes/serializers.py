from rest_framework import serializers
from .models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'full_name', 'phone_number', 'service_type', 'tank_size', 'description', 'created_at']
