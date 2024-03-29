# Generated by Django 2.2.1 on 2019-07-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(unique=True)),
                ('product_name', models.CharField(max_length=255)),
                ('inventory_level', models.IntegerField()),
                ('date', models.DateField()),
                ('test', models.CharField(max_length=255)),
            ],
        ),
    ]
