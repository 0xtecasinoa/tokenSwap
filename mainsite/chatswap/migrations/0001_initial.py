# Generated by Django 4.0.6 on 2022-12-07 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='generalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=20)),
                ('lastLogin', models.DateTimeField(verbose_name='Last Login')),
            ],
        ),
    ]
