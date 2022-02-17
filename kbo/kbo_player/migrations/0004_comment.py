# Generated by Django 3.1.13 on 2022-02-17 08:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kbo_player', '0003_kboplayer_attack_or_attacked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2022, 2, 17, 8, 13, 30, 949096, tzinfo=utc))),
                ('player_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='kbo_player.kboplayer')),
            ],
        ),
    ]