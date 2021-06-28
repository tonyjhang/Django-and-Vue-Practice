# Generated by Django 3.2.4 on 2021-06-28 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TraceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_num', models.CharField(max_length=20)),
                ('stock_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'TraceList',
            },
        ),
        migrations.CreateModel(
            name='TradeDetail',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('stock_num', models.CharField(max_length=20)),
                ('brokerage_name', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('total', models.FloatField()),
                ('buy_avg', models.FloatField()),
                ('buy_quantity', models.IntegerField()),
                ('sell_avg', models.FloatField()),
                ('sell_quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'TradeDetail',
            },
        ),
    ]