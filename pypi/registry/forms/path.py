from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext_lazy as _
from registry import models


class PathForm(forms.ModelForm):
    class Meta:
        model = models.Path
        fields = ['Name', 'FilePath', 'Enabled']
