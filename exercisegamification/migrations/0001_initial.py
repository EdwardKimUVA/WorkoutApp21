# Generated by Django 3.1.6 on 2021-04-13 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphMaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('value', models.IntegerField(verbose_name='value')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True, max_length=30)),
                ('last_name', models.TextField(blank=True, max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('bmi', models.IntegerField(blank=True, null=True)),
                ('fav_exercise', models.TextField(blank=True, max_length=500)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('points_total', models.IntegerField(default=0)),
                ('public', models.BooleanField(default=False)),
                ('private', models.BooleanField(default=True)),
                ('friends', models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_title', models.CharField(max_length=200)),
                ('workout_type', models.CharField(max_length=200)),
                ('workout_description', models.TextField(max_length=500)),
                ('points', models.IntegerField(default=0)),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Workout Completed')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exercisegamification.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('accepted', 'accepted')], max_length=8)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='exercisegamification.profile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='exercisegamification.profile')),
            ],
        ),
        migrations.CreateModel(
            name='MyWorkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myworkout_title', models.CharField(max_length=200)),
                ('myworkout_description', models.TextField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exercisegamification.profile')),
            ],
        ),
        migrations.CreateModel(
            name='MyExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('information', models.TextField(max_length=500)),
                ('myworkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercisegamification.myworkout')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('reach_date', models.DateTimeField(verbose_name='reach date')),
                ('goal_text', models.TextField(blank=True, max_length=50, null=True)),
                ('accomplished', models.BooleanField(verbose_name='have accomplished')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exercisegamification.profile')),
            ],
        ),
    ]