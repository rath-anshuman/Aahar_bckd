from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary

class BHP(models.Model):
    img = CloudinaryField('image', folder='Aahar/BH/', null=True, blank=True)
    public_id = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk and self.public_id and 'img' in self.__dict__:
            cloudinary.uploader.destroy(self.public_id)
        if self.img:
            self.public_id = self.img.public_id  
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.public_id:
            cloudinary.uploader.destroy(self.public_id)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"BHP {self.id} - {self.updated_at}"


class LHP(models.Model):
    img = CloudinaryField('image', folder='Aahar/LH/', null=True, blank=True)
    public_id = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk and self.public_id and 'img' in self.__dict__:
            cloudinary.uploader.destroy(self.public_id)
        if self.img:
            self.public_id = self.img.public_id  
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.public_id:
            cloudinary.uploader.destroy(self.public_id)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"LHP {self.id} - {self.updated_at}"
