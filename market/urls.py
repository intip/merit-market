from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.views import IndexView, TransactionCreateView


urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^transaction/$',
        TransactionCreateView.as_view(), name="transaction"),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
)
