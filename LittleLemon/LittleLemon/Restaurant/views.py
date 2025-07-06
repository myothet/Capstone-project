from django.shortcuts import render

from .models import Menu,Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer,UserRegistrationSerializer
from rest_framework import viewsets
from rest_framework import permissions


from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated,AllowAny

class RegisterUserView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class MenuItemListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class DestroyAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemUpdateView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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
