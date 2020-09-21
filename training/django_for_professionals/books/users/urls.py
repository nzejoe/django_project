from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . views import SignupPageView


urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
]

urlpatterns += staticfiles_urlpatterns()