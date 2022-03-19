# Generated by Django 4.0.3 on 2022-03-19 18:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_blog_options_alter_blogger_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogger',
            options={'ordering': ('user__username',)},
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateField(help_text='The date when the application was sent for consideration')),
                ('motivation', models.TextField(max_length=10000, validators=[django.core.validators.MinLengthValidator(100)])),
                ('status', models.CharField(choices=[('a', 'Accepted'), ('r', 'Rejected'), ('w', 'Awaiting')], help_text='Status of the application', max_length=1)),
                ('user', models.OneToOneField(help_text='User that wants to be an author', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-application_date',),
                'permissions': [('can_approve_application', 'Can approve applications to be an author')],
            },
        ),
    ]
