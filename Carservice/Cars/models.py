from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12,decimal_places=2)
    NEW='New'
    USED='Used'
    CONDITION_CHOICES = [(NEW,'New'),(USED,'Used')]
    condition = models.CharField(max_length=15,choices=CONDITION_CHOICES,default=USED)
    description = models.TextField()
    seller_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID: {self.id} {self.make} {self.model} {self.year} user Id {self.seller_id}"
    
class CarImage(models.Model):
    car = models.ForeignKey(Car,related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return f"User Id: {self.car.seller_id} -> Car Id: {self.car.id}  {self.car.make} {self.car.model} {self.image} Car Obj -> {self.car}"