from django import forms
from models import users
from django.contrib.auth import authenticate, login

class userform(forms.ModelForm):

    first_name = forms.SlugField()
    last_name = forms.SlugField()
    user_name = forms.SlugField()
    Email = forms.EmailField()
    password = forms.CharField()

    class Meta:
        model = users
        fields = ['first_name','last_name','user_name','Email','password']


class loginform(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = users
        fields = ['user_name','password']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user