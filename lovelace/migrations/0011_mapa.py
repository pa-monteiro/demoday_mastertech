# Generated by Django 2.1.7 on 2019-03-17 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lovelace', '0006_auto_20190317_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iluminado', models.CharField(max_length=200)),
                ('movimentado', models.CharField(max_length=200)),
                ('vigilancia', models.CharField(max_length=200)),
                ('seguranca', models.CharField(max_length=200)),
            ],
        ),
    ]
