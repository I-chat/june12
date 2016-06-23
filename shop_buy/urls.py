from django.conf.urls import url

from . import views

app_name = 'shop_buy'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^sell/', views.SellView.as_view(), name='sell'),
    url(r'^(?P<pk>[0-9]+)/product_update', views.ProductUpdate.as_view(), name = 'proupdate'),
    url(r'^merchants_posts', views.merchants_posts, name='merchants'),
    url(r'^categories', views.categories, name='categories'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProductDetails.as_view(), name='details'),
]