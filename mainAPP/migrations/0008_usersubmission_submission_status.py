# Generated by Django 4.0.5 on 2022-07-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPP', '0007_usersubmission_challenge'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubmission',
            name='submission_status',
            field=models.CharField(default='failure', max_length=8),
        ),
    ]