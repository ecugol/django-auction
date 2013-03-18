import importlib
from django.conf import settings
from auction.utils.loader import load_class

BID_ITEM_MODEL = getattr(settings, 'BID_ITEM_MODEL',
    'auction.models.defaults.BidItem')

BidItem = load_class(BID_ITEM_MODEL, 'BID_ITEM_MODEL')