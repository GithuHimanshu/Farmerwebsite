# Generated by Django 5.0.2 on 2024-03-14 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeScreens', '0010_alter_feedback_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='testimonials/'),
        ),
    ]
