# Generated by Django 3.0.8 on 2020-08-06 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200806_1017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('bookId',), 'verbose_name_plural': 'Books'},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_Id',
            new_name='bookId',
        ),
    ]
