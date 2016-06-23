from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.utils import timezone
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import Product_Info

class IndexView(generic.ListView):
    template_name = 'shop_buy/index.html'
    context_object_name = 'latest_product_list'
	
    def get_queryset(self):
        """Return the last five published questions (not including those set to be 
        published in the future)."""
        return Product_Info.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class SellView(LoginRequiredMixin, generic.CreateView):
    model = Product_Info
    fields = ['product_name', 'product_desc', 'product_image', 'product_price']
    success_url = '/shop_buy/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(SellView, self).form_valid(form)

class ProductUpdate(generic.UpdateView):
    model = Product_Info
    fields = ['product_name', 'product_desc', 'product_image', 'product_price']
    template_name = 'shop_buy/product_info_form.html'

    def get_queryset(self):
        """Excludes any Product not created by the logged in user."""
        return Product_Info.objects.filter(created_by = self.request.user)

def merchants_posts(request):
    return HttpResponse("You're looking at merchants posts.")

def categories(request):
    return HttpResponse("You're looking at the categories page.")

class ProductDetails(generic.DetailView):
    template_name = 'shop_buy/detail.html'
    context_object_name = 'product'
    model = Product_Info
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Product_Info.objects.filter(pub_date__lte=timezone.now())