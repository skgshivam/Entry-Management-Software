from django import forms
from .models import *
from dal import autocomplete

class Add_Visitor(forms.ModelForm):
    host = forms.ModelChoiceField(
                queryset=Host.objects.all(),
                widget=autocomplete.ModelSelect2(url='Application:name-autocomplete',
                attrs={
                'data-placeholder': 'Visitor-name',
                #'data-minimum-input-length': 1,
                })
            )
    class Meta:
        model=Visitor
        exclude=['check_out_time']

class ItemForm(forms.ModelForm):
    visitor_name = forms.ModelChoiceField(
                queryset=Host.objects.all(),
                widget=autocomplete.ModelSelect2(url='Application:name-autocomplete',
                attrs={
                'data-placeholder': 'Visitor-name',
                #'data-minimum-input-length': 1,
                })
            )
    class Meta:
        model = Visitor
        fields = '__all__'


