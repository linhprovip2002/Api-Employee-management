# Generated by Django 4.1.7 on 2023-04-04 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]