from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Fertilizer(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("fertilizer-detail", kwargs={"pk": self.id})
    
class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    location = models.CharField(max_length=100)
    
    fertilizers = models.ManyToManyField(Fertilizer)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plant-detail', kwargs={'pk':self.id})
    
class Watering(models.Model):
    WATERING_TYPES = [
        ('Top', 'Top Watered'),
        ('Botton', 'Bottom Watered'),
        ('Mist', 'Misted'),
    ]
    
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='waterings')
    date = models.DateField('Watering Date')
    method = models.CharField(
        max_length=10, 
        choices=WATERING_TYPES, 
        default='Top'
    )
    
    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        return f"{self.date} - {self.method}"
    

    