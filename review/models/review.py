from django.contrib.auth import get_user_model
from django.db import models


class Review(models.Model):
    author = models.ForeignKey(verbose_name='Author', to=get_user_model(), related_name='reviews', null=False, blank=False,on_delete=models.CASCADE)
    product = models.ForeignKey(verbose_name='Product', to='review.Product', related_name='reviews', null=False, blank=False)
    text = models.CharField(verbose_name='Review Text', null=False, blank=False, max_length=1000)

