# Generated by Django 3.1.3 on 2021-07-07 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp2', '0004_auto_20210708_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='retrieval_date',
            field=models.DateTimeField(default='07/08/2021, 03:32:26'),
        ),
    ]
