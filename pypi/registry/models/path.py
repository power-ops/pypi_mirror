from django.db import models
from django.utils.translation import ugettext_lazy as _
from pypi.mixin import MixinManager, MixinQuerySet, MixinModel
from django.core.cache import cache
import os


class PathQuerySet(MixinQuerySet):
    def delete(self):
        for path in self.all():
            if os.path.exists(path.FilePath):
                os.remove(path.FilePath)
        super(MixinQuerySet, self).delete()


class PathManager(MixinManager):
    _queryset = PathQuerySet

    def DeleteUnlinkedFile(self):
        for path in self.get_queryset().filter(package__isnull=True):
            if os.path.exists(path.FilePath):
                os.remove(path.FilePath)


class Path(MixinModel):
    Name = models.CharField(max_length=128, verbose_name=_('Name'))
    FilePath = models.CharField(max_length=128, verbose_name=_('Path'))
    objects = PathManager()

    def __str__(self):
        return self.FilePath

    class Meta:
        verbose_name = _('File Path')
        verbose_name_plural = _('File Path')
