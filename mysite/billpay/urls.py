from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "billpay"),
    path('about/', views.about, name = "AboutUs"),
    path('contact/', views.contact, name = "ContactUs"),
    path('tracker/', views.tracker, name = "TrackingStatus"),
    path('search/', views.search, name = "Search"),
    path('products/<int:myid>', views.prodview, name = "productview"),
    path('checkout/', views.checkout, name = "CheckOut"),
]