# Generated by Django 4.2.2 on 2023-07-18 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='수정일')),
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='작성일')),
                ('title', models.CharField(max_length=20, verbose_name='제목')),
                ('content', models.CharField(max_length=20, verbose_name='내용')),
                ('region', models.CharField(max_length=20, verbose_name='지역')),
                ('user', models.CharField(max_length=20, verbose_name='작성자')),
                ('price', models.IntegerField(default=1000, verbose_name='가격')),
            ],
        ),
    ]
