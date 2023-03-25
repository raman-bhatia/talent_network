# Generated by Django 4.1.7 on 2023-03-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit_activities', '0002_rename_home_function_homefunction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='activity_date',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='activity_objective',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='activity_owner',
        ),
        migrations.AddField(
            model_name='activity',
            name='end_date',
            field=models.DateField(default='2023-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='project_details',
            field=models.TextField(default='provide'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='project_title',
            field=models.CharField(default='Put the title', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='start_date',
            field=models.DateField(default='2023-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='team_members',
            field=models.TextField(default='paln1'),
            preserve_default=False,
        ),
    ]
