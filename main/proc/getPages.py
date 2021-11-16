from django.shortcuts import render
from django.http import HttpRequest
from django.http.response import HttpResponseRedirect


def getIndex(request: HttpRequest) -> render:
    # print(request.path_info)
    return render(request, "index.html")


def redirectToIndex(request: HttpRequest) -> HttpResponseRedirect:
    return HttpResponseRedirect("/")
