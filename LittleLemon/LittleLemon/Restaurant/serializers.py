from rest_framework import serializers

from .models  import Menu,Booking
from django.contrib.auth.models import User, Group
from rest_framework.serializers import ModelSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        customer_group, _ = Group.objects.get_or_create(name='Customer')
        user.groups.add(customer_group)
        return user

class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'  # This will include all fields from the MenuItem model
        # Alternatively, you can specify individual fields like this:
        # fields = ['id', 'name', 'description', 'price', 'available']


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'  # This will include all fields from the Booking model
        # Alternatively, you can specify individual fields like this:
        # fields = ['id', 'name', 'no_of_guests', 'booking_date']

