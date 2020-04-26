# Generated by Django 3.0.5 on 2020-04-26 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20200424_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='user',
        ),
        migrations.AddField(
            model_name='employee',
            name='account_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Account.Account'),
        ),
        migrations.AddField(
            model_name='owner',
            name='account_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Account.Account'),
        ),
    ]