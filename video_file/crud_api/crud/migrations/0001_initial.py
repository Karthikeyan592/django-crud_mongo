# Generated by Django 4.1.13 on 2024-01-23 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('videoId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=500)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]