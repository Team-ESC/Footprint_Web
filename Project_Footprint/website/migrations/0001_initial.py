# Generated by Django 3.0.8 on 2020-07-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beacon_uuid', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=30)),
                ('place_div', models.PositiveSmallIntegerField()),
                ('naver_place_id', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
