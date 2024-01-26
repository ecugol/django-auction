from django.urls import re_path

import auction.views

urlpatterns = [
    re_path(r"^$", auction.views.AuctionListView.as_view(), name="auctions"),
    re_path(r"^bids/$", auction.views.BidListView.as_view(), name="bids"),
    re_path(
        r"^bids/delete/(?P<bid_id>\d+)/$",
        auction.views.BidDetailView.as_view(action="delete"),
        name="delete_bid",
    ),
    re_path(
        r"^auction/(?P<slug>[0-9A-Za-z-_.]+)/$",
        auction.views.AuctionView.as_view(),
        name="auction",
    ),
    re_path(
        r"^auction/(?P<auction_slug>[0-9A-Za-z-_.]+)/lot/(?P<slug>[0-9A-Za-z-_.//]+)/(?P<pk>\d+)/$",
        auction.views.LotDetailView.as_view(),
        name="lot",
    ),
]
