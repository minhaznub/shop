# Generated by Django 3.2 on 2021-04-14 22:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0003_auto_20210414_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Instences',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('Instences_title', models.CharField(max_length=200)),
                ('Instences_description', models.CharField(max_length=200)),
                ('Buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ShopApp.buyer')),
                ('Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ShopApp.product')),
            ],
        ),
    ]
