# Generated by Django 4.1.7 on 2023-03-15 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_weblog', '0010_camping_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
