from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices
class ReviewChoiceForm(TextChoices):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'



class Review(models.Model):
    author = models.ForeignKey(verbose_name='Author', to=get_user_model(), related_name='reviews', null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(verbose_name='Product', to='review.Product', related_name='reviews', null=False, blank=False, on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Review Text', null=False, blank=False, max_length=1000)
    rating = models.CharField(verbose_name='Product Raiting', choices=ReviewChoiceForm.choices, null=True, blank=True, max_length=100, default=ReviewChoiceForm.FIVE)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Created at')
