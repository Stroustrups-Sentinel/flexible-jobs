# Generated by Django 4.1.5 on 2023-07-27 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_generaluserproflie_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationprofile',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='profiles.generaluserproflie'),
            preserve_default=False,
        ),
    ]