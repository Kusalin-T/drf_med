# Generated by Django 4.0.4 on 2022-04-21 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meddoctor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=120)),
                ('lastname', models.CharField(max_length=120)),
                ('nid', models.CharField(default='000000000', max_length=20)),
                ('phonenumber', models.CharField(default='0123456789', max_length=20)),
                ('email', models.EmailField(default='mock@gmail.com', max_length=254)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meddoctor.meddoctor')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
