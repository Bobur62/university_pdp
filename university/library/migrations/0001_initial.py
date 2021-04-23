# Generated by Django 3.1.7 on 2021-03-29 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('author', models.CharField(max_length=512)),
                ('count', models.IntegerField(default=1)),
            ],
        ),
    ]
