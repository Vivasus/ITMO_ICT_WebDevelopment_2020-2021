# Generated by Django 3.1.3 on 2020-11-27 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_first_app', '0004_auto_20201127_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='passport',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
