# Generated by Django 4.0.5 on 2022-06-09 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPP', '0003_alter_problem_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='url',
            field=models.SlugField(unique=True),
        ),
    ]
