from django.contrib import admin

from auction.models import Auction
from auction.models import BidBasket
from auction.models import BidItem
from auction.models import Lot

admin.site.register(BidItem)
admin.site.register(Auction)
admin.site.register(Lot)
admin.site.register(BidBasket)
