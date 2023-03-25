from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from review.forms import ProductForm, ReviewForm
from review.models import Product


class ProductCreateView(CreateView):
    template_name = 'product_add.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(object_list=object_list, **kwargs)
        context['review_form'] = ReviewForm()
        product = self.object
        review = product.reviews.order_by('created_at')
        context['review'] = review
        return context


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'product_update.html'
    form_class = ProductForm
    model = Product
    permission_required = 'review.add_product'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    permission_required = 'review.delete_product'

    def get_success_url(self):
        return reverse('index')