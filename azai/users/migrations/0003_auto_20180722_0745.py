# Generated by Django 2.0.7 on 2018-07-22 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180722_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='ocupacion',
            field=models.ForeignKey(help_text='', null=True, on_delete=django.db.models.deletion.PROTECT, to='users.Ocupacion'),
        ),
    ]