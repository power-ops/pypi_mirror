from registry.models import Path
from django.http import HttpResponse, Http404, HttpResponseForbidden


# Create your views here.
def ViewSet(request):
    Path.objects.DeleteUnlinkedFile()
    return HttpResponse("done")
