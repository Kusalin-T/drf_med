# Generated by Django 4.0.4 on 2022-04-20 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medadmin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medadmin',
            old_name='n_id',
            new_name='nid',
        ),
    ]
