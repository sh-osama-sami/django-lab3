# Generated by Django 4.2.11 on 2024-03-17 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_remove_authors_book'),
        ('books', '0002_alter_books_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authors.authors'),
        ),
    ]
