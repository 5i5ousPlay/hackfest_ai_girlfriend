# Generated by Django 4.2 on 2023-04-18 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='permission_class',
            field=models.CharField(default='UNSUBSCRIBED', max_length=255),
        ),
    ]
