from django import forms
from django.contrib.admin import widgets


class LinkForm(forms.Form):
    link = forms.URLField(
        label="Link with dataset",
        required=True,
    )
