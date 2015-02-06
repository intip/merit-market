from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login
from core.views import IndexView, TransactionCreateView


urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^login/$',
        login,
        kwargs={'template_name': 'index.html'},
        name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^transaction/$', TransactionCreateView.as_view(), name="transaction"),
)
