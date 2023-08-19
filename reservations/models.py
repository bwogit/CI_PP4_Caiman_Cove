from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
custom_time_slots = (
    ('09:00', '09:00 AM'),
    ('12:00', '12:00 PM'),
    ('18:00', '06:00 PM'),
    # Add more time slots as needed
)

status_options = (
    ('Awaiting confirmation', 'Awaiting Confirmation'),
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

    class Meta:
        ordering = ['-capacity']

    def __str__(self):
        return self.table_number


class Customer(models.Model):
    """
    a class for the Customer model
    """
    customer_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=80)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254, default="example@example.com", validators=[EmailValidator()])
    
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.customer_name # Return a meaningful representation, like the customer's name


class Reservation(models.Model):
    """
    A class for the reservation model
    """
    def clean(self):
        if self.reserved_date < timezone.now().date():
            raise ValidationError("Reserved date must be in the future.")


    reservation_id = models.AutoField(primary_key=True)
    reservation_time = models.DateTimeField(auto_now_add=True)
    reserved_date = models.DateField()
    reserved_time_slot = models.CharField(
        max_length=25, choices=custom_time_slots, default='12:00')
    reserved_table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="table_reserved",
        null=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer", null=True)
    reservation_status = models.CharField(max_length=25, choices=status_options, default='awaiting confirmation',  unique=True)
    customer_capacity = (
        (1, "1 Customer"),
        (2, "2 Customers"),
        (3, "3 Customers"),
        (4, "4 Customers"),
        (5, "5 Customers"),
        (6, "6 Customers"),
        )
    customer_count = models.PositiveIntegerField(choices=customer_capacity, default=2) 

    class Meta:
        ordering = ['-reserved_time_slot']

    def __str__(self):
        return str(self.reservation_id)