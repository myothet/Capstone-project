from django.db import models


class Booking(models.Model):
    id=models.IntegerField(primary_key=True, verbose_name="Booking ID")
    name=models.CharField(max_length=255, verbose_name="Customer Name")
    no_of_guests=models.IntegerField(verbose_name="Number of Guests")
    booking_date= models.DateField(verbose_name="Booking Date")
    

    def __str__(self):
        return f"{self.name} - {self.booking_date}"
    




class Menu(models.Model):
    id=models.IntegerField(primary_key=True, verbose_name="Menu Item ID")
    title=models.CharField(max_length=255, verbose_name="Menu Item Title")
    price=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    inventory=models.IntegerField()
   

# Create your models here.
