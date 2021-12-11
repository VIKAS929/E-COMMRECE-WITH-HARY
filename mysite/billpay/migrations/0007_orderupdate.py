# Generated by Django 3.2.7 on 2021-11-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billpay', '0006_alter_order_items_json'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
