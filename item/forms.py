from django import forms

from .models import Item
from .admin import OrderItem
from item.models import Item
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField

""" variáveis para adicionar propriedades de CSS aos campos dos formulários """
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
INPUT_CLASSES_SELECT = 'form-select respiro'
INPUT_CLASSES_TEXT = 'form-control respiro'
INPUT_CLASSES_AREA = 'form-control respiro'
INPUT_CLASSES_DESABILITADO = 'disabled'



class NewItemForm(forms.ModelForm):
    """Classe que representa um Item novo(Publicação nova)"""
    class Meta:
        model = Item
        orderitem = OrderItem
        """Campos do formulário"""
        fields = ('usuario', 'grupo_acesso', 'category', 'name', 'description', 'description_with_photo', 'price', 'image')
        # fields = '__all__'

        readonly_fields = ['created_at', 'usuario']
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
    """Classe criada para editar um Item(publicação)"""
    class Meta:
        model = Item
        fields = ('usuario', 'grupo_acesso', 'name', 'description', 'description_with_photo', 'price', 'image', 'is_sold', 'is_published')
        readonly_fields = ['created_at', 'usuario']

        widgets = {

            'usuario': forms.TextInput(attrs={
                'teste': INPUT_CLASSES_DESABILITADO
            }),

            'grupo_acesso': forms.Select(attrs={
                'class': INPUT_CLASSES_SELECT
            }),

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
            
            'is_published': forms.BooleanField(),

            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class ItemForm(ModelForm):
    """Classe criada para instanciar um objeto do tipo Item(Publicação)"""
    class Meta:
        model = Item
        # fields = ['grupo_acesso', 'category','name','description', 'description_with_photo', 'is_published',  """,'created_by',"""]
        fields = ['grupo_acesso', 'category','name','description', 'description_with_photo', 'is_published', 'created_by',]
        
        readonly_fields = ['created_at', 'usuario']
        
        widgets = {
            
            # 'usuario': forms.TextInput(attrs={
            #     'class': INPUT_CLASSES_DESABILITADO
            # }),

            'grupo_acesso': forms.Select(attrs={
                'class': INPUT_CLASSES_SELECT
            }),
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

            # 'is_published': forms.BooleanField(),
            
            # 'is_published': forms.BooleanField(),

            # 'created_by': forms.Select(attrs={
            #     'class': INPUT_CLASSES_SELECT
            # }),

        }

        def __init__(self, *args, **kwargs):
            super(Item, self).__init__(*args, **kwargs)
            self.fields['category'].error_messages['required'] = u'Nova mensagem de erro.'

