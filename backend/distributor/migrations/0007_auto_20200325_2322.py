# Generated by Django 3.0.4 on 2020-03-25 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0006_auto_20200325_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='needtype',
            name='name_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='needtype',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Name'),
        ),
    ]
