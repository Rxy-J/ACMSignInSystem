"""ACMSignInSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from main.proc import api, getPages

urlpatterns = [
    # path('admin/', admin.site.urls),
    
    # 页面
    # path("getCode/", getPage.getCodePage),
    path("", getPages.getIndex),
    path("login/", getPages.redirectToIndex),
    path("user-info/", getPages.redirectToIndex),
    path("user-train-info/", getPages.redirectToIndex),
    path("team-train-info/", getPages.redirectToIndex),
    path("sign-in-out/", getPages.redirectToIndex),

    # API
    path("api/", api.apiCheck),
    path("api/checkusername/", api.checkUsername),
    path("api/getemailcode/", api.getEmailCode),
    path("api/register/", api.register),
    path("api/login/", api.login),
    path("api/logout/", api.logout),
    path("api/signin/", api.signIn),
    path("api/getcode/", api.getCode),
    path("api/getuserinfo/", api.getUserInfo),
    path("api/getspecificrecord/", api.getSpecificRecord),
    path("api/getrecord/", api.getRecord),
    path("api/getall/", api.getAll),
    # path("api/updatepwd/", api.updatePassword)
    path("api/droprecord/", api.deleteRecord),
    path("api/flushall/", api.flushAll),
    path("invitecode/", api.getInviteCode)
]
