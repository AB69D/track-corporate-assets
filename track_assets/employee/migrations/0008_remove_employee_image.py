# Generated by Django 4.1.7 on 2023-03-08 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_alter_employee_user_device_return'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='image',
        ),
    ]