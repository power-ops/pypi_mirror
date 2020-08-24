from django.contrib import admin
from pypi.mixin import MixinAdmin
from registry import models, forms


@admin.register(models.Path)
class PathAdmin(MixinAdmin):
    list_display = ('Name', 'FilePath', 'Enabled', 'CreateDate')
    list_filter = ('Name', 'Enabled')
    search_fields = ('Name',)
    form = forms.PathForm
    readonly_fields = ('Name', 'FilePath', 'CreateDate')
    ordering = ('-id',)
