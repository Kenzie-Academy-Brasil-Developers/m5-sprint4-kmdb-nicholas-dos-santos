# Generated by Django 4.0.6 on 2022-07-26 23:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=127)),
                ('duration', models.CharField(max_length=10)),
                ('premiere', models.DateField()),
                ('classification', models.IntegerField()),
                ('synopsis', models.TextField()),
                ('genres', models.ManyToManyField(related_name='movies', to='genres.genre')),
            ],
        ),
    ]