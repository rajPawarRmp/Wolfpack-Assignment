# Generated by Django 4.1.4 on 2022-12-31 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgName', models.CharField(max_length=100)),
                ('mainImg', models.ImageField(upload_to='uploads')),
            ],
        ),
    ]