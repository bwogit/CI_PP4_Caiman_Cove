from django.contrib import admin
from .models import Table, Reservation



# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_id', 'table_number', 'capacity')
    list_filter = ('capacity',)
    search_fields = ('table_number',)

# Define the custom admin action function


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
    
    search_fields = ['name']
    actions = ['approve_reservation']

    def approve_reservation(modeladmin, request, queryset):
        queryset.update(status='confirmed')




