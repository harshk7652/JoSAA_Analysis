# Generated by Django 4.1.6 on 2023-03-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_optioninfo_timeperiod'),
    ]

    operations = [
        migrations.AddField(
            model_name='optioninfo',
            name='currentstockprice',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='optioninfo',
            name='strikeprice',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='optioninfo',
            name='timeperiod',
            field=models.IntegerField(),
        ),
    ]
