from django import forms
from .models import *
from dal import autocomplete

class Add_Visitor(forms.ModelForm):
    host = forms.ModelChoiceField(
                queryset=Host.objects.all(),
                widget=autocomplete.ModelSelect2(url='Application:name-autocomplete',
                attrs={
                'data-placeholder': 'Host Name',
                
                #'data-minimum-input-length': 1,
                })
            )
    class Meta:
        model=Visitor
        exclude=['check_out_time']

    def clean(self): 
  
        super(Add_Visitor, self).clean() 
          
        mobile_no = self.cleaned_data.get('phone') 
        # text = self.cleaned_data.get('text') 
  
        if len(str(mobile_no)) != 10: 
            self._errors['phone'] = self.error_class([ 
                'Mobile No Length must be 10']) 
          
        # return any errors if found 
        return self.cleaned_data         




