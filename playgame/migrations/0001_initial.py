# Generated by Django 2.0.2 on 2018-03-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('player_1', models.TextField()),
                ('player_2', models.TextField()),
                ('won', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
