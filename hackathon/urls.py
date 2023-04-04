from django.urls import path
from .views import CreateHackathonView,GetAdminHackathonView, MakeFavouritesView, GetHackathonView, GetAllFavouriteView, GetHackathonByIdView

urlpatterns = [
    path('create', CreateHackathonView.as_view()),
    path('admin/get', GetAdminHackathonView.as_view()),
    path('favourites/add', MakeFavouritesView.as_view()),
    path('favourites', GetAllFavouriteView.as_view()),
    path('<int:id>',GetHackathonByIdView.as_view()),
    path('', GetHackathonView.as_view()),

]
