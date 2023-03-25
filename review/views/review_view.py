from django.urls import reverse
from django.views.generic import FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect

from review.forms import ReviewForm
from review.models import Product, Review


class ReviewCreateView(LoginRequiredMixin, FormView):
    form_class = ReviewForm

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        author = request.user
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            Review.objects.create(author=author, text=text, product=product)
        return redirect('product_detail', pk=product.pk)

class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'review_update.html'
    form_class = ReviewForm
    model = Review
    permission_required = 'review.update_review'

    def get_success_url(self):
        return reverse('index')

class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    model = Review
    template_name = 'review_delete.html'
    permission_required = 'review.delete_review'

    def get_success_url(self):
        return reverse('index')