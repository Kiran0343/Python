from django import forms
from models import users


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

    def __unicode__(self):
        return self.email