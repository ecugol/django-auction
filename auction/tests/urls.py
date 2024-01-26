"""
This ``urls.py`` is only used when running the tests via ``runtests.py``.
As you know, every app must be hooked into yout main ``urls.py`` so that
you can actually reach the app's views (provided it has any views, of course).

"""
from django.urls import include, path
from django.conf.urls import patterns


urlpatterns = patterns(
    "",
    path("", include("auction.urls")),
)
