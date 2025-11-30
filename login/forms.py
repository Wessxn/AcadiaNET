from django import forms
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label='Username', widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True, label='Password')
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'major', 'username', 'password']
        
        def save(self, commit=True):
            profile = super().save(commit=False)
            profile.set_password(self.cleaned_data["password"])
            if commit:
                profile.save()
            return profile
            
class PasswordResetForm(forms.Form):
    email = forms.EmailField(required=True, label='Email Address', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if email.strip() == "":
            raise forms.ValidationError('Email cannot be empty.')
    
class EnterCode(forms.Form):
    code = forms.CharField(max_length=6, min_length=6, required=True, label='Verification Code')
    
    def clean_code(self):
        code = self.cleaned_data['code']
        if not code.isdigit():
            raise forms.ValidationError('Code must be numeric.')
        return code

