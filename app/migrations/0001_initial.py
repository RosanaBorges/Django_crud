# Generated by Django 3.2.8 on 2021-10-23 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('NomeCliente', models.CharField(max_length=150)),
                ('CPF', models.CharField(max_length=11)),
                ('Endereco', models.CharField(max_length=100)),
                ('Celular', models.CharField(max_length=11)),
                ('Email', models.EmailField(max_length=10)),
            ],
        ),
    ]
