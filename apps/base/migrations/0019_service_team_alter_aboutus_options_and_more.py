# Generated by Django 5.0.3 on 2024-03-25 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_banner_options_alter_aboutus_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание услуги')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('photo', models.ImageField(upload_to='Участники')),
                ('job', models.CharField(max_length=255, verbose_name='Должность')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('twitter', models.URLField(verbose_name='Twitter')),
                ('pinterest', models.URLField(verbose_name='Pinterest')),
                ('facebook', models.URLField(verbose_name='Facebook')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команда',
            },
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.AlterModelOptions(
            name='admin',
            options={'verbose_name': 'Админ', 'verbose_name_plural': 'Админ'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакт'},
        ),
        migrations.AlterModelOptions(
            name='contactpost',
            options={'verbose_name': 'Контактные Брони', 'verbose_name_plural': 'Контактные Брони'},
        ),
        migrations.AlterModelOptions(
            name='footer',
            options={'verbose_name': 'Нижняя Информация', 'verbose_name_plural': 'Нижняя Информации'},
        ),
        migrations.AlterModelOptions(
            name='footerpost',
            options={'verbose_name': 'Бронированные', 'verbose_name_plural': 'Бронированные'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='background',
            field=models.ImageField(upload_to='back_about_us', verbose_name='Фон'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image_1',
            field=models.ImageField(upload_to='about_us', verbose_name='Фото 1'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image_2',
            field=models.ImageField(upload_to='about_us', verbose_name='Фото 2'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='location',
            field=models.CharField(max_length=255, verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='phone',
            field=models.CharField(max_length=30, verbose_name='Телефонный номер'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='background',
            field=models.ImageField(upload_to='Баннер', verbose_name='Фон'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image_1',
            field=models.ImageField(upload_to='Фото_1', verbose_name='Фото 1'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image_2',
            field=models.ImageField(upload_to='Фото_2', verbose_name='Фото 2'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='main_image',
            field=models.ImageField(upload_to='Главное Фото', verbose_name='Главное Фото'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='mini_description',
            field=models.TextField(verbose_name='Мини-Описание'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='quote',
            field=models.TextField(verbose_name='Цитаты'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='background',
            field=models.ImageField(upload_to='Контакт', verbose_name='Фон'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='contactpost',
            name='fullname',
            field=models.CharField(max_length=255, verbose_name='Полное Имя'),
        ),
        migrations.AlterField(
            model_name='contactpost',
            name='message',
            field=models.TextField(verbose_name='Сообщения'),
        ),
        migrations.AlterField(
            model_name='contactpost',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Телефонный номер'),
        ),
        migrations.AlterField(
            model_name='contactpost',
            name='theme',
            field=models.CharField(max_length=100, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='image',
            field=models.ImageField(upload_to='Нижняя', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='mini_description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='footerpost',
            name='adults_quantity',
            field=models.IntegerField(verbose_name='Количество взрослых'),
        ),
        migrations.AlterField(
            model_name='footerpost',
            name='childs_quantity',
            field=models.IntegerField(verbose_name='Количество детей'),
        ),
        migrations.AlterField(
            model_name='footerpost',
            name='date',
            field=models.CharField(max_length=30, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='footerpost',
            name='fullname',
            field=models.CharField(max_length=255, verbose_name='Полное Имя'),
        ),
        migrations.AlterField(
            model_name='footerpost',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Телефонный номер'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='Новости', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]