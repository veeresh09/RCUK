# Generated by Django 3.0.2 on 2020-05-25 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rcutting', '0005_auto_20200525_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rcform',
            name='applicnt_email',
            field=models.CharField(default='NULL', max_length=1000),
        ),
    ]
