from django.contrib import admin
from pypi.mixin import MixinAdmin
from registry import models, forms


@admin.register(models.Package)
class PackageAdmin(MixinAdmin):
    list_display = ('Name', 'Enabled', 'CreateDate')
    list_filter = ('Name', 'Enabled')
    search_fields = ('Name',)
    form = forms.PackageForm
    readonly_fields = ('Name', 'Path', 'CreateDate',)
    ordering = ('-id',)
