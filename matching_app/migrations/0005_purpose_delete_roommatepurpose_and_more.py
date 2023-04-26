# Generated by Django 4.1.7 on 2023-03-21 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching_app', '0004_roommatepurpose_remove_roommatepreference_lifestyle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='RoommatePurpose',
        ),
        migrations.AlterField(
            model_name='roommatepreference',
            name='purpose',
            field=models.ManyToManyField(choices=[('study', '勉強'), ('work', '仕事'), ('hobby', '趣味'), ('other', 'その他')], to='matching_app.purpose', verbose_name='目的'),
        ),
    ]
