from django.views.generic import ListView

from review.models import Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'product'
    queryset = Product.objects.all()
    paginate_by = 2
    paginate_orphans = 1
    ordering = ('name', 'category')
