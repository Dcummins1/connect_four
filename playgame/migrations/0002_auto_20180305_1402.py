# Generated by Django 2.0.2 on 2018-03-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playgame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player_2',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='won',
            field=models.TextField(null=True),
        ),
    ]