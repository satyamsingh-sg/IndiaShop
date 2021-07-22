# Generated by Django 3.0.7 on 2021-07-18 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_auto_20210717_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderplaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('exp', models.DateField()),
                ('deliver', models.CharField(choices=[('Confirmed', 'Confirmed'), ('Packed', 'Packed'), (' courier', ' courier'), ('picked_up', 'picked_up')], max_length=30)),
                ('costomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Customers')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Orderplace',
        ),
    ]
