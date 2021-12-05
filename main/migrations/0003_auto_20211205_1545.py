# Generated by Django 3.2.9 on 2021-12-05 15:45

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_hitslog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hitslog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='short_code',
            field=models.CharField(db_index=True, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.CharField(max_length=10000, validators=[main.validators.valid_URL]),
        ),
    ]