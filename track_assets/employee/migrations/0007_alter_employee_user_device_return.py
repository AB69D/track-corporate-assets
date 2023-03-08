# Generated by Django 4.1.7 on 2023-03-08 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_device_user_alter_device_amount_alter_device_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0006_payment_way'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Device_Return',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('device_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.device')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]