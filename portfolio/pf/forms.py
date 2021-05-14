from django import forms
from django.forms import ModelForm

from pf.models import Catagory, Blog, Message, User

#Form for creating a new blog catagory
class BlogForm(UserCreationForm):
    #form fields
    blogName = forms.CharField(max_length=100, required=True)
    catagories = tags = forms.ModelMultipleChoiceField(queryset=Catagory.objects.all(),
        widget=forms.CheckboxSelectMultiple, required=Treu, label="Catagories")

    class Meta:
        model = Blog
        fields = ['blogName', 'catagories']
        help_texts = {
            'blogName': "Name For the Blog",
            'catagories': "Catagories Relevant to Blog Being Created."
        }
