from django.urls import path
from .views import bhp_view, lhp_view

urlpatterns = [
    path('bhp/', bhp_view, name='bhp-view'),  # Single view for BHP
    path('lhp/', lhp_view, name='lhp-view'),  # Single view for LHP
]
