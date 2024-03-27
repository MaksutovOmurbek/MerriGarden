# Generated by Django 5.0.3 on 2024-03-26 17:15

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_team_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='service_image/', verbose_name='Фото')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание услуги')),
            ],
            options={
                'verbose_name': 'Услуга 2',
                'verbose_name_plural': 'Услуги 2',
            },
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Наша команда', 'verbose_name_plural': 'Наша команда'},
        ),
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='team',
            name='job',
        ),
        migrations.RemoveField(
            model_name='team',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='team',
            name='pinterest',
        ),
        migrations.RemoveField(
            model_name='team',
            name='twitter',
        ),
        migrations.AddField(
            model_name='team',
            name='descriptions',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='team/', verbose_name='Фотография'),
        ),
        migrations.AddField(
            model_name='team',
            name='whatsapp',
            field=models.URLField(blank=True, null=True, verbose_name='Whatspp URL'),
        ),
        migrations.AddField(
            model_name='team',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='Youtube URL'),
        ),
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='team',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook URL'),
        ),
        migrations.AlterField(
            model_name='team',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram URL'),
        ),
    ]
