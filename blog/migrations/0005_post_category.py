# Generated by Django 2.2.1 on 2022-08-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_video_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('football', 'Football'), ('badminton', 'Badminton'), ('swimming', 'Swimming'), ('basketball', 'Basketball'), ('volleyball', 'Volleyball'), ('table-tennis', 'Table Tennis')], default='football', max_length=20),
        ),
    ]
