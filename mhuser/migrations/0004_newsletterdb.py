# Generated by Django 4.1.7 on 2023-08-23 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhuser', '0003_applicantdb_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletterdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
