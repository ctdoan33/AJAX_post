from django import forms
from models import *

class PostForm(forms.Form):
    add_a_note = forms.CharField(max_length=255, widget=forms.Textarea)