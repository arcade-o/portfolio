from .models import profile, project
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import profile

class add_project(forms.ModelForm):
    class Meta:
        model = project
        fields = ("name","github",)

    widgets = {
        
        "name": forms.TextInput(attrs={'class': 'form-control'}),
        "github": forms.URLField(),

        }
    

class profileCreationForm(UserCreationForm):

    class Meta:
        model = profile
        fields = ("email",)

class profileChangeForm(UserChangeForm):

    class Meta:
        model = profile
        fields = ("email",)