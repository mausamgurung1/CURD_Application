# Generated by Django 4.2.11 on 2024-05-01 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_mobile_number_user_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.IntegerField(max_length=15),
        ),
    ]
