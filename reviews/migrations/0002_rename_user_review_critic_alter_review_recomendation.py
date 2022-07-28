# Generated by Django 4.0.6 on 2022-07-27 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='critic',
        ),
        migrations.AlterField(
            model_name='review',
            name='recomendation',
            field=models.CharField(choices=[('Must Watch', 'Must'), ('Should Watch', 'Should'), ('Avoid Watch', 'Avoid'), ('No option', 'No')], default='No option', max_length=50),
        ),
    ]