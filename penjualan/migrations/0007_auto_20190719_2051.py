# Generated by Django 2.2 on 2019-07-19 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penjualan', '0006_auto_20190718_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaksi',
            name='waktu',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 19, 20, 51, 32, 214717)),
        ),
    ]
