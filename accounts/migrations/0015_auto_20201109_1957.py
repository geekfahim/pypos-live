# Generated by Django 3.0.7 on 2020-11-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20201109_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appconfig',
            name='app_name',
            field=models.CharField(default='pypos', max_length=200, null=True, unique=True),
        ),
    ]
