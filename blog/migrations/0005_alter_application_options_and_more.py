# Generated by Django 4.0.3 on 2022-03-20 00:31

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_application_application_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ('-application_date_time',), 'permissions': [('can_approve_application', 'Can approve applications to be an author')]},
        ),
        migrations.RemoveField(
            model_name='application',
            name='application_date',
        ),
        migrations.AddField(
            model_name='application',
            name='application_date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='When the application was sent for consideration'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='motivation',
            field=models.TextField(help_text='Why you are going to write as an author. Describe yourself and your experience', max_length=10000, validators=[django.core.validators.MinLengthValidator(100)]),
        ),
    ]
