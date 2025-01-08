from django.contrib import admin
from django.urls import path,include

from .views import aaa
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('schdl.urls')),
    path('',aaa)
]
