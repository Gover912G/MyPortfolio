# Generated by Django 5.2.3 on 2025-07-02 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField(default='text')),
                ('category', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(upload_to='vesitables')),
            ],
        ),
    ]
