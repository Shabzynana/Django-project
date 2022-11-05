# Generated by Django 4.1.2 on 2022-11-04 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("date_released", models.DateTimeField()),
                ("likes", models.IntegerField()),
                (
                    "artist_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="musicapp_api.artist",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lyric",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                (
                    "song_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="musicapp_api.song",
                    ),
                ),
            ],
        ),
    ]
