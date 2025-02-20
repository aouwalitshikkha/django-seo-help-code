from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponsePermanentRedirect
import re

class TrailingSlashMiddleware(MiddlewareMixin):
    def process_request(self, request):
        path = request.path_info
        if re.search(r'\.[^/]+$', path):
            return None
        if re.search(r'\.[^/]+/$', path):
            return HttpResponsePermanentRedirect(path[:-1])
        if not path.endswith('/'):
            return HttpResponsePermanentRedirect(path + '/')
        return None
