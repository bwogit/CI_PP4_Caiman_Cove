from django.contrib import admin
from .models import Table, Reservation, Customer

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_id', 'table_number', 'capacity')
    list_filter = ('capacity',)
    search_fields = ('table_number',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_id','reservation_time', 'reserved_date', 'reserved_time_slot', 'reserved_table', 'customer', 'reservation_status','customer_count')
    list_filter = ('reservation_id','reservation_time', 'reserved_date', 'reserved_time_slot', 'reserved_table', 'customer', 'reservation_status','customer_count')
    search_fields = ('reserved_table__table_number', 'customer__customer_name')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'phone', 'email', 'created_date')
    search_fields = ('customer_name', 'email')


