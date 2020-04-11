# Generated by Django 3.0.5 on 2020-04-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='seller_name',
            field=models.CharField(default='NULL', max_length=200),
        ),
        migrations.AddField(
            model_name='seller',
            name='seller_password',
            field=models.CharField(default='NULL', max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_name',
            field=models.CharField(default='NULL', max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_password',
            field=models.CharField(default='NULL', max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_price',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='order',
            name='history',
            field=models.CharField(default='NULL', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='seller',
            name='balance',
            field=models.FloatField(default=1.0),
        ),
    ]
