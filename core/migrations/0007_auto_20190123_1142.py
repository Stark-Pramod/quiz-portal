# Generated by Django 2.0.6 on 2019-01-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190123_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='university_roll_no',
            field=models.CharField(max_length=10),
        ),
    ]
