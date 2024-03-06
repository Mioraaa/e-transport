

from rest_framework import serializers

from .models import Destination, Seats, Customer, Bagages, Driver


class DestinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destination
        fields = ['id', 'start_at', 'end_at', 'costs']
        
class SeatSerializer(serializers.ModelField):

    class meta():
        model = Seats
        fields = ['seats_total', 'seats_used', 'seats_free', 'get_seats_choices']
        

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['first_phone_number', 'second_phone_number', 'customer_name', 'cin', 'seats']
        

class BagagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bagages
        fields = ['customer', 'weigth', 'costs', 'bagage_name', 'description']


class DriverSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'phone_number', 'image']