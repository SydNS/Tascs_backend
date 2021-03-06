# Generated by Django 3.1.5 on 2021-01-25 05:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TascsUAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('lastname', models.CharField(max_length=20, unique=True)),
                ('Uemail', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('residence', models.CharField(max_length=30)),
                ('country_of_origin', models.CharField(max_length=30)),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('reg_date',),
            },
        ),
    ]
