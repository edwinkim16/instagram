# Generated by Django 3.2.8 on 2021-10-17 05:58

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('bio', models.CharField(max_length=200)),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('followers', models.ManyToManyField(blank=True, default=0, related_name='profile_followers', to='instagram.Profile')),
                ('following', models.ManyToManyField(blank=True, default=0, related_name='profile_following', to='instagram.Profile')),
            ],
        ),
    ]