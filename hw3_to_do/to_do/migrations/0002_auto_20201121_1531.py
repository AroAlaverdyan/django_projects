# Generated by Django 3.1.3 on 2020-11-21 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newtodo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newtodo',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='newtodo',
            name='notification',
            field=models.IntegerField(choices=[(0, 'Allow'), (1, "Don't Allow")], default='0'),
        ),
        migrations.AlterField(
            model_name='newtodo',
            name='status',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Doing'), (2, 'Done')]),
        ),
    ]
