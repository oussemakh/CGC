# Generated by Django 2.1 on 2018-10-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='learn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('disc', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('img', models.ImageField(blank=True, default='defualt.png', upload_to='')),
                ('file', models.FileField(upload_to='')),
                ('slug2', models.SlugField(blank=True, null=True)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]