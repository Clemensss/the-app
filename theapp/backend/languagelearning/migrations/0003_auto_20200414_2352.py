# Generated by Django 3.0.5 on 2020-04-14 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languagelearning', '0002_auto_20200414_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='relatedTexts',
        ),
        migrations.AddField(
            model_name='text',
            name='words',
            field=models.ManyToManyField(default='', to='languagelearning.Word'),
        ),
    ]
