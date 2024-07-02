from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}

class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        email = forms.EmailField(required=True)
        def clean(self, email):
            super(SignInForm, self).clean()
            if email:
                self.user_cache = authenticate(
                    self.request, 
                    username=email, 
                    password=self.cleaned_data.get('password')               
                    
                )
                if self.user_cache is None:
                    raise forms.ValidationError(
                        'Invalid email or password'
                    )
            return self.cleaned_data