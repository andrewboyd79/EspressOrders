# Generated by Django 3.0 on 2021-09-22 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
