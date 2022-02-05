# Generated by Django 4.0.2 on 2022-02-05 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=1024)),
                ('active', models.BooleanField(default=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
