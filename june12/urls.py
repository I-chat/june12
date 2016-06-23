"""june12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views
from shop_buy import account_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shop_buy/', include('shop_buy.urls')),
    url(r'^accounts/profile/$', account_views.UserProfileView.as_view(), name='profile'),
    url(r'^accounts/profile/update/', account_views.ProfileFormView.as_view(), name='update'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^media/(?P<path>.*)$', views.serve)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)