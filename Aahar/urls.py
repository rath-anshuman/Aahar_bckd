from django.contrib import admin
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from account.views import login,logout
from Aahar import views
from account.views import add_visitor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('schdl.urls')),
    path('',views.abc,name='abc'),
    path('visit/',add_visitor,name='VISITOR'),
    path('login/',csrf_exempt(login)),
    path('logout/',csrf_exempt(logout)),
]



