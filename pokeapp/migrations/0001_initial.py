# Generated by Django 2.0.7 on 2018-07-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('blood_type', models.CharField(max_length=50)),
                ('favorite_food', models.CharField(max_length=50)),
            ],
        ),
    ]
