from django import forms
from .models import Books, Category
class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'title',
            'author',
            'book_photo',
            'author_photo',
            'price',
            'retal_price',
            'retal_peiod',
            'total_retal',
            'pages',
            'status',
            'category',
        ]


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'book_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'author_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'retal_price': forms.NumberInput(attrs={'class': 'form-control rentalprice'}),
            'retal_peiod': forms.NumberInput(attrs={'class': 'form-control dayperiod'}),
            'total_retal': forms.NumberInput(attrs={'class': 'form-control totalrental'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }