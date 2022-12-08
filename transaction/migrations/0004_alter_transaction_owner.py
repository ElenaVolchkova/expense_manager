# Generated by Django 4.1.3 on 2022-12-08 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0003_remove_owner_transaction_owner_user'),
        ('transaction', '0003_transaction_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='owner.owner'),
        ),
    ]
