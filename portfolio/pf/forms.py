from django import forms
from django.forms import ModelForm

from pf.models import Catagory, Blog, Message, User

#Form for creating a new blog catagory
class BlogForm(ModelForm):
    #form fields
    blogName = forms.CharField(max_length=100, required=True, help_text="Name For the Blog",
        label="Blog Name")
    catagories = forms.ModelMultipleChoiceField(queryset=Catagory.objects.all(),
        widget=forms.CheckboxSelectMultiple, required=True, label="Catagories",
        help_text="Catagories Relevant to Blog Being Created")

    class Meta:
        model = Blog
        fields = ['blogName', 'catagories']
