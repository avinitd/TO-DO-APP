# Generated by Django 3.0.7 on 2020-06-10 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='category',
            field=models.ForeignKey(default='general', on_delete=django.db.models.deletion.DO_NOTHING, to='todolist.Category'),
        ),
    ]
