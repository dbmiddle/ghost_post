from django import forms
from gposts.models import BoastsAndRoasts


class AddPostForm(forms.Form):
    is_boast = forms.BooleanField(initial=False, required=False)
    content = forms.CharField(widget=forms.Textarea)
