from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User

custom_time_slots = (
    ('12:00', '12:00 PM'),
    ('13:00', '13:00 PM'),
    ('17:00', '17:00 PM'),
    ('18:00', '18:00 PM'),
    ('19:00', '19:00 PM'),
    ('20:00', '21:00 PM'),
    ('22:00', '22:00 PM'),
    ('23:00', '23:00 PM'),
   
)

status_options = (
    ('awaiting confirmation', 'Awaiting Confirmation'),
    ('confirmed', 'Confirmed'),
    ('rejected', 'Rejected'),
    ('expired', 'Expired'),
)


class Table(models.Model):
    """
    A class for the Table model(table)
    """
    table_id = models.AutoField(primary_key=True)
    table_number = models.CharField(
        max_length=10, default='New Table', unique=True)
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    reserved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-capacity']

    def __str__(self):
        return self.table_number

class Reservation(models.Model):
    """
    A class for the reservation model
    """
    reservation_id = models.AutoField(primary_key=True)
    reservation_time = models.DateTimeField(auto_now_add=True)
    reserved_date = models.DateField()
    reserved_time_slot = models.CharField(
        max_length=25, choices=custom_time_slots, default='12:00')
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name="table_reserved",
        null=True
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True)
    name = models.CharField(
        max_length=50,
        null=True
        )
    email = models.EmailField(
        max_length=254,
        default=""
        )
    phone = PhoneNumberField(null=True)
    status = models.CharField(
        max_length=25,
        choices=status_options,
        default='awaiting confirmation'
        )
    seats = (
        (1, "1 Guest"),
        (2, "2 Guests"),
        (3, "3 Guests"),
        (4, "4 Guests"),
        (5, "5 Guests"),
        (6, "6 Guests"),
        )
    guest_count = models.IntegerField(choices=seats, default=2)

    class Meta:
        ordering = ['-reserved_time_slot']
        unique_together = ('reserved_date', 'reserved_time_slot', 'table')

    def __str__(self):
        return self.status
        