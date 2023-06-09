# Generated by Django 4.1.7 on 2023-03-23 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='day_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profession',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='self_introduction',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_last_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
