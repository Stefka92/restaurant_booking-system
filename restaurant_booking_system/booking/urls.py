from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('restaurant-list/', views.restaurant_list, name='restaurant_list'),
    path('make-reservation/', views.make_reservation, name='make_reservation'),
    path('reservation-success/', views.reservation_success, name='reservation_success'),
    path('class-based-restaurant-list/', views.RestaurantListView.as_view(), name='class_based_restaurant_list'),
    path('class-based-reservation-success/', views.ReservationSuccessView.as_view(), name='class_based_reservation_success'),
]

