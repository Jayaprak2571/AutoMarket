from django.db import models

# Create your models here.
class TestDrive(models.Model):
    user_id = models.IntegerField()
    vehicle_id = models.IntegerField()
    seller_id = models.IntegerField()
    scheduled_date = models.DateTimeField()
    PENDING='Pending'
    CONFIRMED='Confirmed'
    CANCELLED='Cancelled'
    STATUS_CHOICES =[
        (PENDING,'Pending'),
        (CONFIRMED,'Confirmed'),
        (CANCELLED,'Cancelled'),
    ]
    status = models.CharField(max_length=15,choices=STATUS_CHOICES,default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Test Drive for User {self.user_id} -> {self.vehicle_id} on {self.scheduled_date}"