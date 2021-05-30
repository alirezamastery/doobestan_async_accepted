# Generated by Django 3.1.3 on 2021-05-30 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('manager_name', models.CharField(default='', max_length=200)),
                ('manager_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('manager_name', models.CharField(default='', max_length=200)),
                ('manager_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('nationalID', models.CharField(max_length=200)),
                ('illName', models.CharField(max_length=200)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sicks', to='doob.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('nationalID', models.CharField(max_length=200)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='doob.company')),
            ],
        ),
    ]
