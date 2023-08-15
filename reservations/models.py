from django.db import models

# Create your models here.
class Table(models.Model):
    """
    class for the Table model(table)
    """
    table_id = models.AutoField(primary_key=True)
    table_number = models.CharField(
        max_length=10, default='New Table', unique=True)
    capacity = models.PositiveIntegerField()

    class Meta:
        ordering = ['-capacity']

    def __str__(self):
        return self.table_name