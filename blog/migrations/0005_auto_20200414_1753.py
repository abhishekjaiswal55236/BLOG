# Generated by Django 2.2 on 2020-04-14 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200414_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.ImageField(default='', upload_to='media/images/'),
        ),
    ]
