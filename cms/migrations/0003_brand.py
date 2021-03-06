# Generated by Django 2.1.5 on 2019-01-13 01:59

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20190106_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='')),
            ],
        ),
    ]
