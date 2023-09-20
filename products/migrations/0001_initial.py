# Generated by Django 4.0.2 on 2023-09-20 05:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.TextField(blank=True)),
                ('price', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, upload_to='product/product_cover/', verbose_name='Product Image')),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Time of Creation')),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
