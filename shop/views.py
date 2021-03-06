from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from core.mixins import LoginRequiredMixin

from .forms import ProductForm
from .models import Product

class ProductListView(LoginRequiredMixin, ListView):
    context_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(
            stok__gt=0
        )


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('shop:product_list')

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(ProductCreateView, self).post(
                request, *args, **kwargs
            )
        return HttpResponseForbidden()

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(ProductCreateView, self).get(
                request, *args, **kwargs
            )
        return HttpResponseForbidden()
