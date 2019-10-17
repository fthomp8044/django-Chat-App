from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
#meta provides extra info about this particular class we are createing. its a django syntax
    class Meta:
        # model equeals CustomUser from models.py
        model = CustomUser
        # below is a tupel vvvvv, make sure to add commas
        fields = ('username', 'email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

#
# class ProfileCreationForm(UserCreationForm):
#     #meta provides extra info about this particular class we are createing. its a django syntax
#     class Meta:
#
#         model = Profile
#         fields= ('User', 'bio', 'location')
