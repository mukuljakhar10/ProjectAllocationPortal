# Generated by Django 5.1.3 on 2024-11-14 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_of_joining',
            field=models.DateField(blank=True, null=True),
        ),
    ]
