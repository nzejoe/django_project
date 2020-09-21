from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . views import HomepageView, AboutPageView


urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about')
]

urlpatterns += staticfiles_urlpatterns()