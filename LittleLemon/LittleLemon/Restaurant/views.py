from django.shortcuts import render

from .models import Menu,Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer
from rest_framework import viewsets


from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

class MenuItemListView(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class DestroyAPIView(DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemUpdateView(UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class SingleBookingView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingCreateView(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingUpdateView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class  BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer




# Create your views here.
def index(request):
    return render(request, 'index.html', {})
# Create your views here.
