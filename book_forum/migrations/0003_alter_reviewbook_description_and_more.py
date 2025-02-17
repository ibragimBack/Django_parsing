# Generated by Django 5.0.3 on 2024-03-28 17:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_forum', '0002_alter_book_forum_book_reviewbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewbook',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='reviewbook',
            name='name_correction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='book_forum.book_forum'),
        ),
        migrations.AlterField(
            model_name='reviewbook',
            name='stars',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
