# Generated by Django 4.2 on 2023-08-18 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicesapp', '0002_remove_services_id_services_contactnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='AboutCook',
            field=models.CharField(max_length=500),
        ),
    ]
