from django.urls import path
from .views import Home, ShoeList, ShoeDetail, WornDetail, WornListCreate, ShoelaceList, ShoelaceDetail, AddShoelaceToShoe, RemoveShoelaceFromShoe

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('shoes/', ShoeList.as_view(), name='shoe-list'),
    path('shoes/<int:id>/', ShoeDetail.as_view(), name='shoe-detail'),
    path('shoes/<int:shoe_id>/worn/', WornListCreate.as_view(), name='worn-list-create'),
    path('shoes/<int:shoe_id>/worn/<int:id>/', WornDetail.as_view(), name='worn-detail'),
    path('shoelaces/', ShoelaceList.as_view(), name='shoelace-list'),
    path('shoelaces/<int:id>/', ShoelaceDetail.as_view(), name='shoelace-detail'),
    path('shoes/<int:shoe_id>/add_shoelaces/<int:shoelace_id>/', AddShoelaceToShoe.as_view(), name='add-shoelace-to-shoe'),
    path('shoes/<int:shoe_id>/remove_shoelaces/<int:shoelace_id>/', RemoveShoelaceFromShoe.as_view(), name='remove-shoelace-from-shoe')
]