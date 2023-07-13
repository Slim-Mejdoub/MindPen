# Generated by Django 4.2.1 on 2023-06-24 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('mood_score', models.IntegerField()),
            ],
        ),
    ]
