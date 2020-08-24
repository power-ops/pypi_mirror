from pypi.utils import log
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.conf import settings
import urllib.request
import os
from registry.models import Package
from django.core.cache import cache


# Create your views here.
@log.log()
def ViewSet(request, path, subpath):
    if request.method == 'GET':
        if subpath == 'simple':
            rr = cache.get(path)
            if rr:
                return HttpResponse(rr)
            try:
                r = urllib.request.urlopen(settings.MIRROR + path)
                rr = r.read()
                cache.set(path, rr)
                return HttpResponse(rr)
            except:
                raise Http404()
        filedir, filename = os.path.split(os.path.join(settings.CACHE_DIR, path))
        filepath = os.path.join(filedir, filename)
        package, t = Package.objects.create_or_get(filename, filepath)
        if not package.Enabled:
            return HttpResponseForbidden()
        try:
            os.makedirs(filedir)
        except:
            pass
        if os.path.isfile(filepath):
            return HttpResponse(open(filepath, 'rb'))
        else:
            r = urllib.request.urlopen(settings.MIRROR + path)
            fd = os.open(filepath, os.O_RDWR | os.O_CREAT)
            os.write(fd, r.read())
            os.close(fd)
            return HttpResponse(open(filepath, 'rb'))
    raise Http404()
