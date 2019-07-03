# Generated by Django 2.2 on 2019-06-18 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0004_auto_20190618_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listbarang',
            name='jumlah',
        ),
        migrations.RemoveField(
            model_name='listbarang',
            name='waktu',
        ),
        migrations.AlterField(
            model_name='listbarang',
            name='nama',
            field=models.TextField(max_length=30),
        ),
        migrations.CreateModel(
            name='LogBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.IntegerField()),
                ('waktu', models.DateTimeField()),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produksi.ListBarang')),
            ],
        ),
    ]
