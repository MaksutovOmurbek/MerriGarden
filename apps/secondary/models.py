from django.db import models


# Create your models he
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name='Фотография ')


    class Meta:
        verbose_name = ' Галерея'
        verbose_name_plural = 'Галерея'