from django.contrib import admin
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from account.views import login,logout
from Aahar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('schdl.urls')),
    path('',views.abc,name='abc'),
    path('login/',login),
    path('logout/',logout),
]



