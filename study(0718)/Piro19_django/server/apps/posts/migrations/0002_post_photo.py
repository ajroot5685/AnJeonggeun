# Generated by Django 4.2.2 on 2023-07-18 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name='이미지'),
        ),
    ]
