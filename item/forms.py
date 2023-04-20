from django import forms

from .models import Item
from .admin import OrderItem
from item.models import Item
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
INPUT_CLASSES_SELECT = 'form-select respiro'
INPUT_CLASSES_TEXT = 'form-control respiro'
INPUT_CLASSES_AREA = 'form-control respiro'


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
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES_SELECT
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES_TEXT
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES_AREA
            }),
            'description_with_photo': RichTextUploadingField({
                'class': INPUT_CLASSES_SELECT
            }),
            'created_by': forms.Select(attrs={
                'class': INPUT_CLASSES_SELECT
            }),
        }

        def __init__(self, *args, **kwargs):
            super(Item, self).__init__(*args, **kwargs)
            self.fields['category'].error_messages['required'] = u'Nova mensagem de erro.'

