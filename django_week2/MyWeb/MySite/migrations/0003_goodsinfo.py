# Generated by Django 3.0.7 on 2020-06-28 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0002_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('goods_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('goods_number', models.IntegerField()),
                ('goods_price', models.FloatField()),
            ],
        ),
    ]
