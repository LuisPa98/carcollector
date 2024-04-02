# Generated by Django 5.0.3 on 2024-04-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=350)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
