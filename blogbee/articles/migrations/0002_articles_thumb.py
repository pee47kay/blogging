# Generated by Django 4.0.1 on 2022-06-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='Thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
