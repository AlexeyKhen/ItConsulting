# Generated by Django 3.1.1 on 2020-09-18 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200918_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
