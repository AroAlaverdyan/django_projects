# Generated by Django 3.1.3 on 2020-11-18 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('notification', models.IntegerField(choices=[(0, 'Allow'), (1, "Don't Allow")])),
                ('status', models.IntegerField(choices=[(0, 'New'), (0, 'Doing'), (0, 'Done')])),
            ],
        ),
    ]