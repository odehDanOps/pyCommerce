# Generated by Django 3.1.6 on 2021-06-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210626_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='created_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bids',
            name='updated_at',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='created_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='updated_at',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listings',
            name='created_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listings',
            name='updated_at',
            field=models.TimeField(blank=True, null=True),
        ),
    ]