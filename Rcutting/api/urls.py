from django.urls import path
from Rcutting.api.views import UserlistView, RCformlistview

urlpatterns = [
    path("users/", UserlistView.as_view(), name="user-list"),
    path("forms/", RCformlistview.as_view(), name="Rcform - list")
]
