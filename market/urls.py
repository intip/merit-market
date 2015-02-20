from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.views import TransactionCreateView


urlpatterns = patterns(
    '',
    url(r'^transaction/$',
        TransactionCreateView.as_view(), name="transaction"),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login',
        kwargs={'template_name': 'core/login.html'}, name="login"),

    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        kwargs={'login_url': '/login/'}, name='logout'),
)
