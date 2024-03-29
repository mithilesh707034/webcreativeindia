# Generated by Django 3.2.20 on 2024-02-10 08:25

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='uploads')),
                ('title', models.CharField(max_length=100)),
                ('description', tinymce.models.HTMLField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
