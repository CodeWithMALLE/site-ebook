# Generated by Django 4.2.1 on 2023-05-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_rename_commandes_panier_articles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panier',
            name='commandee',
        ),
        migrations.RemoveField(
            model_name='panier',
            name='date_commande',
        ),
        migrations.AddField(
            model_name='article',
            name='date_commande',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
