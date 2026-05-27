from django.db import models
from django.core.validators import MinValueValidator


class Medicine(models.Model):
    UNIT_CHOICES = (
        ('VIEN', 'Viên'),
        ('VI', 'Vỉ'),
        ('LO', 'Lọ'),
        ('CHAI', 'Chai'),
        ('TUYP', 'Tuýp'),
    )
    
    medicine_id = models.AutoField(primary_key=True)
    medicine_name = models.CharField(max_length=200)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='VIEN')
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    stock_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'Medicines'
        ordering = ['medicine_name']
    
    def __str__(self):
        return f"{self.medicine_name} ({self.unit})"