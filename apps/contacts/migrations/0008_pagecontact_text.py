# Generated by Django 5.0 on 2023-12-27 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_alter_pagecontact_email_alter_pagecontact_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecontact',
            name='text',
            field=models.CharField(default=1, max_length=255, verbose_name='Описание текста'),
            preserve_default=False,
        ),
    ]