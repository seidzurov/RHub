# Generated by Django 4.2.4 on 2023-08-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_publications_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='likes',
            field=models.IntegerField(default=True),
        ),
    ]
