# Generated by Django 5.0.3 on 2024-04-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_shoelace'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='shoelace',
            field=models.ManyToManyField(to='main_app.shoelace'),
        ),
        migrations.AlterField(
            model_name='worn',
            name='age',
            field=models.CharField(choices=[('<1', 'Less than a year old'), ('2-4', 'Between 2-4 years old'), ('5+', 'More than 5 years old')], default='<1', max_length=5),
        ),
    ]