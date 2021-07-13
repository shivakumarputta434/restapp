# Generated by Django 3.1.3 on 2021-07-06 21:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newapp2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('releasedate', models.DateTimeField(default=django.utils.timezone.now)),
                ('featured', models.BooleanField(default=False)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='newapp2.category')),
                ('product_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_color', to='newapp2.color')),
            ],
        ),
    ]