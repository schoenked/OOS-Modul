# Generated by Django 2.2.1 on 2019-05-22 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESA2', '0005_auto_20190523_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lehrveranstaltung',
            name='teilnehmer',
            field=models.ManyToManyField(to='ESA2.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='lehrveranstaltungen',
            field=models.ManyToManyField(to='ESA2.Lehrveranstaltung'),
        ),
        migrations.DeleteModel(
            name='Einschreibung',
        ),
    ]
