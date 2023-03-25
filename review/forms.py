from django import forms
from django.core.validators import BaseValidator, MinLengthValidator

from .models import Product, Review




class CustomLenValidator(BaseValidator):
    def __init__(self, limit_value=500):
        message = 'You can only write 500 symbols'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        print(value)
        print(limit_value)
        return value > limit_value

    def clean(self, value):
        return len(value)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category')
        labels = {
            'name': 'Name',
            'description': 'Description',
            'image': 'Image',
            'category': 'Category',
        }

class ReviewForm(forms.ModelForm):
    text = forms.CharField(required=True, widget=forms.Textarea, validators= (MinLengthValidator(limit_value=2, message='Your review is too short'), CustomLenValidator()))
    class Meta:
        model = Review
        fields = ('rating', 'text', )
