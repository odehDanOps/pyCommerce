# Generated by Django 3.1.6 on 2021-06-14 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title to be displayed for the listing', max_length=64)),
                ('description', models.CharField(help_text="A description that lets users know more about what you're selling!", max_length=225)),
                ('starting_bid', models.DecimalField(decimal_places=2, help_text='What is the starting price you want to sell your product for? All prices are in NGN!', max_digits=8)),
                ('image_url', models.CharField(blank=True, help_text='Enter image URL', max_length=1024)),
                ('category', models.CharField(blank=True, help_text='Enter category e.g. Fashion, Toys, Electronics, Home, etc.', max_length=64)),
                ('closed', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
                ('watchlist_users', models.ManyToManyField(blank=True, related_name='watchlist_items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=225)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.listings')),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_offer', models.DecimalField(decimal_places=2, help_text='How much are you willing to pay for this item?', max_digits=8)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.listings')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids_made', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
