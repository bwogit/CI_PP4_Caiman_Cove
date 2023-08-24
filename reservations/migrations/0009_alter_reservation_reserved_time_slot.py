# Generated by Django 3.2.20 on 2023-08-24 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0008_auto_20230823_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reserved_time_slot',
            field=models.CharField(choices=[('12:00', '12:00 PM'), ('13:00', '13:00 PM'), ('17:00', '17:00 PM'), ('18:00', '18:00 PM'), ('19:00', '19:00 PM'), ('20:00', '21:00 PM'), ('22:00', '22:00 PM'), ('23:00', '23:00 PM')], default='12:00', max_length=25),
        ),
    ]
