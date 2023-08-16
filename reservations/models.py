from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

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
    capacity = models.PositiveIntegerField()

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
    reserved_table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="table_reserved",
        null=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="user", null=True)
    reservation_status = models.CharField(max_length=25, choices=status_options, default='awaiting confirmation',  unique=True)
    customer_capacity = (
        (1, "1 Customer"),
        (2, "2 Customers"),
        (3, "3 Customers"),
        (4, "4 Customers"),
        (5, "5 Customers"),
        (6, "6 Customers"),
        )
    class Meta:
        ordering = ['-reserved_time_slot']

    def __str__(self):
        return str(self.reservation_id)


class customer(models.Model):
    """
    a class for the User model
    """
    user_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=80)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254, default="example@example.com")
    
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.user_id