from django.db import models
from django.utils.translation import ugettext_lazy as _
from pypi.mixin import MixinManager, MixinQuerySet, MixinModel
from django.core.cache import cache
from .path import Path


class PackageQuerySet(MixinQuerySet):
    pass


class PackageManager(MixinManager):
    _queryset = PackageQuerySet

    def create_or_get(self, name, path):
        return self.get_or_create(Name=name, Path=Path.objects.get_or_create(Name=name, FilePath=path)[0])


class Package(MixinModel):
    Name = models.CharField(max_length=128, verbose_name=_('Name'))
    Path = models.ForeignKey(Path, on_delete=models.CASCADE)

    objects = PackageManager()

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _('Package')
        verbose_name_plural = _('Package')
        # permissions = [('view_self_asset', 'Can view self assets')]

    def disable(self):
        self.Enabled = False
        self.save()
        cache.set('forbidden packages', self.objects.filter(Enabled=False))

    def enable(self):
        self.Enabled = True
        self.save()
        cache.set('forbidden packages', self.objects.filter(Enabled=False))
