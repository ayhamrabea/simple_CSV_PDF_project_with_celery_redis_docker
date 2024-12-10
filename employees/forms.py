from django import forms
from .models import Employ


class Add_employ(forms.ModelForm):
    class Meta:
        model = Employ
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'age' : forms.TextInput(attrs={'class':'form-control'}),
            'job_title' : forms.TextInput(attrs={'class':'form-control'}),
            'status' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'addres' : forms.TextInput(attrs={'class':'form-control'}),
            'bio' : forms.Textarea(attrs={'class':'form-control'}),
        }
