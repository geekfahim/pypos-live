# Generated by Django 3.0.7 on 2020-11-03 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20201029_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Brand'),
        ),
    ]