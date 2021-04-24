from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import GroceryItem, GroceryList

class GroceryItemForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = '__all__'
        exclude = ('owner',)
        widgets = {'description': forms.Textarea(attrs={'cols': 80, 'rows': 3})}


class GroceryListForm(forms.ModelForm):
    class Meta:
        model = GroceryList 
        fields = '__all__'