# Generated by Django 2.1.5 on 2019-03-08 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20190307_1937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='vehicle',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]