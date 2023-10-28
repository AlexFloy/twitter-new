# Generated by Django 4.2.6 on 2023-10-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users/profile_images')),
                ('data_joined', models.DateField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
