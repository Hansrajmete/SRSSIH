# Generated by Django 2.0.2 on 2018-03-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRS', '0005_auto_20180311_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
