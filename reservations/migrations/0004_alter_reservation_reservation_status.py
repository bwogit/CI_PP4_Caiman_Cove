# Generated by Django 3.2.20 on 2023-08-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_reservation_customer_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_status',
            field=models.CharField(choices=[('Awaiting confirmation', 'Awaiting Confirmation'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected'), ('expired', 'Expired')], default='awaiting confirmation', max_length=25),
        ),
    ]
