# Generated by Django 3.2.6 on 2021-09-07 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b2project', '0006_auto_20210907_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='EndDate',
            field=models.DateTimeField(verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='StartDate',
            field=models.DateTimeField(verbose_name='Start Date'),
        ),
    ]
