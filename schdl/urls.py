from django.urls import path
from .views import bhp_view, lhp_view

from account.views import visitorplus

urlpatterns = [
    path('bhp/', bhp_view, name='bhp-view'),  
    path('lhp/', lhp_view, name='lhp-view'),  
    path('visitor/', visitorplus, name='visitorplus'),
]
