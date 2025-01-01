from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary

class BHP(models.Model):
    img = CloudinaryField('image', folder='Aahar/BH/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"BHP {self.id} - {self.updated_at}"
class LHP(models.Model):
    img = CloudinaryField('image', folder='Aahar/LH/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"LHP {self.id} - {self.updated_at}"
