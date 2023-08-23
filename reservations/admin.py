from django.contrib import admin
from .models import Table, Reservation

# Define the custom admin action function
def approve_reservations(modeladmin, request, queryset):
    queryset.update(reservation_status='confirmed')
approve_reservations.short_description = "Approve selected reservations"

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_id', 'table_number', 'capacity')
    list_filter = ('capacity',)
    search_fields = ('table_number',)

# @admin.register(Reservation)
# class ReservationAdmin(admin.ModelAdmin):
#     list_display = ('reservation_id','reservation_time', 'reserved_date', 'reserved_time_slot', 'customer', 'reservation_status','customer_count')
#     list_filter = ('reservation_status',)
#     actions = ['approve_reservations']
#     search_fields = ('reserved_table__table_number', 'customer__customer_name')
# Registration of bookings to display in the admin panel

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_filter = (
        'user',
        'name',
        'email',
        'phone',
        'guest_count',
        'status',
        'table_id',
        'reserved_date', 
        'reserved_time_slot',
        'reservation_time',
        )
    list_display = (
        'reservation_id',
        'user',
        'name',
        'phone',
        'guest_count',
        'status',
        'table',
        'reserved_date', 
        'reserved_time_slot',
        'reservation_time',)
    
    actions = ['confirm_bookings']


# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('customer_id', 'customer_name', 'phone', 'email', 'created_date')
#     search_fields = ('customer_name', 'email')


