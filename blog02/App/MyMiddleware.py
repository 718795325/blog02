
from django.shortcuts import redirect

from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if request.user.is_authenticated:
            return
        elif request.path == '/zhuce/':
            return
        elif request.path !='/loginb/':
            return redirect('/loginb/')

