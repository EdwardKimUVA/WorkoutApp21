# Generated by Django 3.1.7 on 2021-05-05 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercisegamification', '0017_workout_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='workouts/'),
        ),
    ]