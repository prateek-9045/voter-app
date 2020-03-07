"""voterapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
#from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token
from voter import views
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('voter-details/', views.VoterDetailsView.as_view(), name='voter-details'),
    path('customer-details/', views.CustomerDetailsView.as_view(), name='customer-details'),
    path('assembly/', views.AssemblyView.as_view(), name='assembly'),
    path('election/', views.ElectionView.as_view(), name='election'),
    path('app-download/', views.AppDownloadView.as_view(), name='app-download'),
    path('extended-data/', views.ExtendedDataView.as_view(), name='extended-data'),

]
