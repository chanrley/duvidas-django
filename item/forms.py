from django import forms

from .models import Item
from .admin import OrderItem
from item.models import Item
from django.forms import ModelForm
# from ckeditor_uploader import RichTextUploadingField


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        orderitem = OrderItem
        # fields = ('category', 'name', 'description', 'description_with_photo', 'price', 'image')
        fields = '__all__'

        readonly_fields = ['created_at']
        # widgets = {
        #     'category': forms.Select(attrs={
        #         'class': INPUT_CLASSES
        #     }),
        #     'name': forms.TextInput(attrs={
        #         'class': INPUT_CLASSES
        #     }),
        #     'description': forms.Textarea(attrs={
        #         'class': INPUT_CLASSES
        #     }),
            
        #     'description_with_photo': RichTextUploadingField(attrs={
        #         'class': INPUT_CLASSES
        #     }),

        #     'image': forms.FileInput(attrs={
        #         'class': INPUT_CLASSES
        #     }),
        #     'price': forms.TextInput(attrs={
        #         'class': INPUT_CLASSES
        #     }),
        #     'created_at': forms.FileInput(attrs={
        #         'class': INPUT_CLASSES
        #     }),  
        # }
        arquivo =  forms.FileField()
          
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'description_with_photo', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'description_with_photo': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['category','name','description', 'description_with_photo', 'created_by']




