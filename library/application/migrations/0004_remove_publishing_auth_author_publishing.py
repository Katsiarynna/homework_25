# Generated by Django 4.2.5 on 2023-11-08 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_create_publishing_models'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publishing',
            name='auth',
        ),
        migrations.AddField(
            model_name='author',
            name='publishing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.publishing'),
        ),
    ]
