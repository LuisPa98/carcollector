from django.urls import path
from .views import Home, ShoeList, ShoeDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('shoes/', ShoeList.as_view(), name='shoe-list'),
    path('shoes/<int:id>/', ShoeDetail.as_view(), name='shoe-detail'),
]