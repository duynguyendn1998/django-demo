# Generated by Django 3.2.9 on 2021-12-09 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20211207_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=1024),
        ),
    ]