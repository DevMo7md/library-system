# Generated by Django 5.0.3 on 2024-03-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_books_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='total_retal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]