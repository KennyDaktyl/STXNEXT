# Generated by Django 3.0.8 on 2020-08-06 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20200806_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributevalue',
            name='attribute_value_dict',
            field=models.TextField(blank=True, null=True),
        ),
    ]
