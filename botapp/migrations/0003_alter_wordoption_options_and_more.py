# Generated by Django 5.0.1 on 2024-09-18 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0002_category_usercategory_word_userword_wordoption'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wordoption',
            options={'verbose_name': 'Word Option', 'verbose_name_plural': 'Word Options'},
        ),
        migrations.AlterUniqueTogether(
            name='wordoption',
            unique_together={('word', 'option', 'is_correct')},
        ),
    ]
