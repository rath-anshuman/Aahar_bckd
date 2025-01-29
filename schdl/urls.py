from django.urls import path
from .views import bhp_get_view,lhp_get_view,bhp_post_view,lhp_post_view

from account.views import visitorplus

urlpatterns = [
    path('bhpget/', bhp_get_view, name='bhp-get-view'),
    path('bhppost/', bhp_post_view, name='bhp-post-view'),
    path('lhpget/', lhp_get_view, name='lhp-get-view'),
    path('lhppost/', lhp_post_view, name='lhp-post-view'),
    path('visitor/', visitorplus, name='visitorplus'),
]
