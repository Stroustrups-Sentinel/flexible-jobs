# Generated by Django 4.1.5 on 2023-07-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaluserproflie',
            name='phoneNumber',
            field=models.CharField(default='+263 xxx xxx xxxx', max_length=25),
        ),
    ]