# Generated by Django 4.1 on 2024-02-05 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_unit_max_rated_power'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequencyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sample_time', models.DateTimeField()),
                ('quality', models.CharField(max_length=20)),
                ('derived_quality', models.CharField(max_length=20)),
            ],
        ),
    ]
