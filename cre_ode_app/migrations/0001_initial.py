# Generated by Django 2.0 on 2018-12-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiffEq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lhs', models.TextField()),
                ('rhs', models.IntegerField()),
                ('parameter', models.IntegerField()),
                ('init_cond', models.IntegerField()),
                ('test_range', models.IntegerField()),
            ],
        ),
    ]
