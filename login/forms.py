from django import forms 

class getCode(forms.Form):
    code = forms.CharField(max_length=6, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter verification code'}))
