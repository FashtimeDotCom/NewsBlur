from django.conf.urls import url, patterns
from apps.oauth import views
from oauth2_provider import views as op_views

urlpatterns = patterns('',
    url(r'^twitter_connect/?$', views.twitter_connect, name='twitter-connect'),
    url(r'^facebook_connect/?$', views.facebook_connect, name='facebook-connect'),
    url(r'^appdotnet_connect/?$', views.appdotnet_connect, name='appdotnet-connect'),
    url(r'^twitter_disconnect/?$', views.twitter_disconnect, name='twitter-disconnect'),
    url(r'^facebook_disconnect/?$', views.facebook_disconnect, name='facebook-disconnect'),
    url(r'^appdotnet_disconnect/?$', views.appdotnet_disconnect, name='appdotnet-disconnect'),
    url(r'^follow_twitter_account/?$', views.follow_twitter_account, name='social-follow-twitter'),
    url(r'^unfollow_twitter_account/?$', views.unfollow_twitter_account, name='social-unfollow-twitter'),

    # Django OAuth Toolkit
    url(r'^authorize/?$', op_views.AuthorizationView.as_view(), name="ifttt-authorize"),
    url(r'^token/?$', op_views.TokenView.as_view(), name="ifttt-token"),
)
