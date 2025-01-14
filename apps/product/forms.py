from django import forms
from apps.product.models import Product,ProductCategory, ProductImage

class ProductForm(forms.ModelForm):
    categories = forms.ModelChoiceField(
        queryset=ProductCategory.objects.all(),
        required=False,
        empty_label = "Select a Category",
        widget=forms.Select(
            attrs={'class': "form-control",}
        )
    )
    
    name = forms.CharField(
        required=False, 
        label='Name',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Name'}),
        error_messages={
            'required': "The name field is required."
        }
    )
    description = forms.CharField(
        required=False, 
        label='Description',
        widget=forms.Textarea(
            attrs={'class': "form-control ",
                   'placeholder': 'Description'}),
        error_messages={
            'required': "The description field is required."
        }
    )

    image = forms.ImageField(
        widget=forms.FileInput(
            attrs = {"id" : "image_field" ,
                    "style" : "height: 100px ; width : 100px "
                    }
            )
    )

    price = forms.CharField(
        required=False, 
        label='Price',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Price'}),
        error_messages={
            'required': "The price field is required."
        }
    )
    brand_name = forms.CharField(
        required=False, 
        label='Brand name',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Brand name'}),
        error_messages={
            'required': "The brand name field is required."
        }
    )



    
    class Meta:
        model = Product
        fields = ['categories', 'name', 'description', 'image', 'price', 'brand_name']



class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        required=False, 
        label='Name',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Name'}),
        error_messages={
            'required': "The name field is required."
        }
    )

    class Meta:
        model = ProductCategory
        fields = ['name']

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = ProductImage
        fields = ['image']


