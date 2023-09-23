# Generated by Django 4.2.2 on 2023-06-26 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(max_length=20)),
                ('datecreated', models.DateField()),
                ('shippinglocation', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dateadded', models.DateField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='useraccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('datecreated', models.DateField()),
                ('email', models.CharField(max_length=50)),
                ('buyerseller', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='userprofiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=1000)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finalexam.useraccounts')),
            ],
        ),
    ]