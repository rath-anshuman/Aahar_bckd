from django.contrib import admin
from django.urls import path,include

from Aahar import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('schdl.urls')),
    path('',views.abc,name='abc'),
]
