# Generated by Django 5.1 on 2024-08-21 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='unique_code',
            field=models.CharField(blank=True, help_text='Необязательно', max_length=16, null=True, unique=True),
        ),
    ]
