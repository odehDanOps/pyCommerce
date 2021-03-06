from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class User(AbstractUser):
    pass

# auction listings
class Listings(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_listings", null=True)
    title = models.CharField(max_length=64, help_text="The title to be displayed for the listing")
    description = models.CharField(max_length=225, help_text="A description that lets users know more about "
                                                              "what you're selling!")
    starting_bid = models.DecimalField(max_digits=8, decimal_places=2, help_text="What is the starting price you want "
                                                                                 "to sell your product for? All "
                                                                                 "prices are in NGN!")
    image_url = models.CharField(max_length=1024, blank=True, help_text="Enter image URL")
    category = models.CharField(max_length=64, blank=True, help_text="Enter category e.g. "
                                                                        "Fashion, Toys, Electronics, Home, etc.")
    watchlist_users = models.ManyToManyField(User, blank=True, related_name="watchlist_items")
    closed = models.BooleanField(default=False)
    created_at = models.DateField(null=True, blank=True)
    updated_at = models.TimeField(null=True, blank=True)

    def current_price(self):
        return max([bid.value_offer for bid in self.bids.all()]+[self.starting_bid])

    def no_of_bids(self):
        return len(self.bids.all())

    def current_winning_bidder(self):
        return self.bids.get(value_offer=self.current_price()).user if self.no_of_bids() > 0 else None

    def __str__(self):
        return f'{self.title} by {self.owner}: {self.description}'

# bids
class Bids(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="bids")
    value_offer = models.DecimalField(max_digits=8, decimal_places=2, help_text="How much are you willing to pay for "
                                                                                "this item?")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids_made")
    created_at = models.DateField(null=True, blank=True)
    updated_at = models.TimeField(null=True, blank=True)

    def clean(self):
        print(self.value_offer)
        print(self.listing.current_price())
        if self.value_offer and self.listing.current_price():
            if self.value_offer <= self.listing.current_price():
                raise ValidationError({'value_offer': _('Please make sure your bid value is higher than the current '
                                                        'price of the item!')})

    def __str__(self):
        return f"{self.user} offers to pay ${self.value_offer} for the listing: {self.listing}"

# comments
class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=225)
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateField(null=True, blank=True)
    updated_at = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.author} says {self.content} for listing: {self.listing}"