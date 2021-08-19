from django.db import models
from django.db.models.fields.files import ImageField

class Sliders(models.Model):
    image = models.ImageField(upload_to='catalog/images', verbose_name='Картинка для слайдера')
