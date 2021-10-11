# Generated by Django 3.2.8 on 2021-10-11 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_item_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_customer', to='myapp.customer'),
        ),
    ]
