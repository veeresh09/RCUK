from django.urls import path
from Rcutting.api.views import UserlistView, RCformlistview, getConsumerCode, paymentView
from Rcutting.api.view2 import Collectpay
urlpatterns = [
    path("users/", UserlistView.as_view(), name="user-list"),
    path("forms/", RCformlistview.as_view(), name="Rcform - list"),
    path("consumCode/", getConsumerCode.as_view(), name="ConsumeCOde"),
    path("pay/", paymentView.as_view(), name="paymentpage"),
    path("collect/", Collectpay.as_view(), name="collectionpage")
]
