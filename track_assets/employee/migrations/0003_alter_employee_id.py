# Generated by Django 4.1.7 on 2023-03-02 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20230302_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
