from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
class Admin(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    phone = models.CharField(max_length=30, verbose_name='Телефонный номер')
    email = models.EmailField(verbose_name='Email')
    location = models.CharField(max_length=255, verbose_name='Локация')
    instagram = models.URLField(verbose_name='Instagram')
    twitter = models.URLField(verbose_name='Twitter')
    youtube = models.URLField(verbose_name='YouTube')
    facebook = models.URLField(verbose_name='Facebook')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Админ'
        verbose_name_plural = 'Админ'

class Banner(models.Model):
    id =  models.IntegerField(primary_key= True, blank= True, null= False, verbose_name= 'ID')
    banner_title = models.CharField(max_length=25, verbose_name='Название Баннера')
    banner_text = models.TextField(verbose_name='Текст Баннера')
    price = models.IntegerField(verbose_name='Цена')
    background = models.ImageField(upload_to='Баннер', verbose_name='Фон')
    main_image = models.ImageField(upload_to='Главное Фото', verbose_name='Главное Фото')
    quote = models.TextField(verbose_name="Цитаты")
    image_1 = models.ImageField(upload_to='Фото_1', verbose_name='Фото 1')
    image_2 = models.ImageField(upload_to='Фото_2', verbose_name='Фото 2')
    mini_description = models.TextField(verbose_name='Мини-Описание')

    def __str__(self) -> str:
        return f"News {self.banner_title}"
    
    class Meta:
        verbose_name = 'Баннера'
        verbose_name_plural = 'Баннеры'

class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    background = models.ImageField(upload_to='back_about_us', verbose_name='Фон')
    image_1 = models.ImageField(upload_to='about_us', verbose_name='Фото 1')
    image_2 = models.ImageField(upload_to='about_us', verbose_name='Фото 2')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='Новости', verbose_name='Фото')

    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

class Contact(models.Model):
    id =  models.IntegerField(primary_key= True, blank= True, null= False, verbose_name= 'ID')
    background = models.ImageField(upload_to='Контакт', verbose_name='Фон')
    description = models.TextField(verbose_name='Описание')

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакт'

class ContactPost(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='Полное Имя')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=100, verbose_name='Телефонный номер')
    theme = models.CharField(max_length=100, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщения')

    def __str__(self) -> str:
        return self.fullname
    
    class Meta:
        verbose_name = 'Контактные Брони'
        verbose_name_plural = 'Контактные Брони'

class Footer(models.Model):
    id =  models.IntegerField(primary_key= True, blank= True, null= False, verbose_name= 'ID')
    image = models.ImageField(upload_to='Нижняя', verbose_name='Фото')
    mini_description = models.TextField(verbose_name='Описание')

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Нижняя Информация'
        verbose_name_plural = 'Нижняя Информации'

class FooterPost(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='Полное Имя')
    phone = models.CharField(max_length=100, verbose_name='Телефонный номер')
    date = models.CharField(max_length=30, verbose_name='Дата')
    adults_quantity = models.IntegerField(verbose_name='Количество взрослых')
    childs_quantity = models.IntegerField(verbose_name='Количество детей')

    def __str__(self) -> str:
        return self.fullname
    
    class Meta:
        verbose_name = 'Бронированные'
        verbose_name_plural = 'Бронированные'

           
class Team(models.Model):
    image = ResizedImageField(force_format="WEBP", quality=100, upload_to='team/',verbose_name="Фотография",blank = True, null = True)
    title = models.CharField( max_length=255, verbose_name="Имя")
    email = models.EmailField(verbose_name="Почта",blank=True,null=True)
    descriptions = models.TextField(verbose_name="Описание")
    whatsapp = models.URLField(verbose_name='Whatspp URL',blank=True, null=True )
    instagram = models.URLField(verbose_name='Instagram URL',blank=True, null=True )
    youtube = models.URLField(verbose_name='Youtube URL',blank=True, null=True )
    facebook = models.URLField(verbose_name='Facebook URL',blank=True, null=True)
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Наша команда"
            verbose_name_plural = "Наша команда"

class Service(models.Model):
    description = models.TextField(verbose_name= 'Описание услуги')


    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'