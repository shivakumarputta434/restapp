# Generated by Django 3.1.3 on 2021-07-08 16:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp2', '0008_auto_20210708_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='retrieval_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 8, 22, 12, 36, 71178)),
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=250)),
                ('areacolor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='areacolor', to='newapp2.color')),
            ],
        ),
    ]
