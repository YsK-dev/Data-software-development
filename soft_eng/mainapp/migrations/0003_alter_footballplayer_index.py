# Generated by Django 5.1.3 on 2024-12-29 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_footballplayer_opa_footballplayer_att_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footballplayer',
            name='index',
            field=models.IntegerField(unique=True),
        ),
    ]
