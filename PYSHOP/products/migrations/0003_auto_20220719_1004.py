# Generated by Django 3.1.4 on 2022-07-19 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='item',
        ),
    ]
