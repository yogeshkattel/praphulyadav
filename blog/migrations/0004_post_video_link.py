# Generated by Django 2.2.1 on 2022-08-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]