# Generated by Django 2.2.12 on 2020-06-05 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_county', models.CharField(max_length=50)),
                ('number_of_cases', models.IntegerField()),
            ],
        ),
    ]
