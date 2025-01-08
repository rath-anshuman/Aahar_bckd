from django.contrib import admin
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from account.views import token_obtain,token_refresh
from Aahar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('schdl.urls')),
    path('',views.abc,name='abc'),
    path('api/token/', csrf_exempt(token_obtain), name='token_obtain'),
    path('api/token-refresh/', csrf_exempt(token_refresh), name='token_refresh'),
]



