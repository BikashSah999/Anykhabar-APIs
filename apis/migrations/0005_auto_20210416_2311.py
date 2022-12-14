# Generated by Django 3.0.8 on 2021-04-16 17:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='posted_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comments',
            name='mail_address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comments',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
