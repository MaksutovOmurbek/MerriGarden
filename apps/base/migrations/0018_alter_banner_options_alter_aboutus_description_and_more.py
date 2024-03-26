# Generated by Django 5.0.3 on 2024-03-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_footerpost_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'Баннера', 'verbose_name_plural': 'Баннеры'},
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image_1',
            field=models.ImageField(upload_to='about_us', verbose_name='вдьа'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_text',
            field=models.TextField(verbose_name='Текст Баннера'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_title',
            field=models.CharField(max_length=25, verbose_name='Название Баннера'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]