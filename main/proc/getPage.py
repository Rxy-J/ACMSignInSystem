from datetime import datetime
from django.shortcuts import render

def getCodePage(request):
    request.session["time"] = datetime.now().strftime("%Y%m%d%H%M%S")
    return render(request, "getCode.html")

def getLoginPage(request):
    request.session["time"] = datetime.now().strftime("%Y%m%d%H%M%S")
    return render(request, "login.html")