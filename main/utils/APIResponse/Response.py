
from django.http import HttpRequest
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound

class APIUtils():
    def __init__(self, request: HttpRequest):
        self.request = request
        
        if request.method == "GET":
            self.dataDict = request.GET.dict()
        elif request.method == "POST":
            self.dataDict = request.POST.dict()
        else:
            self.dataDict = {}