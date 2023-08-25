from django.contrib import admin
from .models import Table, Reservation

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Table model.
    Displays table information in the admin panel.
    """
    list_display = ('table_id', 'table_number', 'capacity')
    list_filter = ('capacity',)
    search_fields = ('table_number',)

# Define the custom admin action function
def approve_reservation(modeladmin, request, queryset):
    """
    Custom admin action to approve reservations in bulk.
    Changes the status of selected reservations to 'confirmed'.
    """
        queryset.update(status='confirmed')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Reservation model.
    Displays reservation information in the admin panel.
    Provides a custom admin action to approve reservations.
    """
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
    
    search_fields = ['name']
    actions = ['approve_reservation']

    




