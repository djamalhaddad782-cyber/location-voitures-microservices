from django.urls import path
from .views import BookingViewSet, AdminBookingViewSet

booking_list = BookingViewSet.as_view({'get': 'list', 'post': 'create'})
booking_detail = BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
booking_cancel = BookingViewSet.as_view({'post': 'cancel'})

admin_accept = AdminBookingViewSet.as_view({'patch': 'accept'})
admin_refuse = AdminBookingViewSet.as_view({'patch': 'refuse'})
admin_car_taken = AdminBookingViewSet.as_view({'patch': 'car_taken'})
admin_complete = AdminBookingViewSet.as_view({'patch': 'complete'})

urlpatterns = [
    path('bookings/', booking_list, name='booking-list'),
    path('bookings/<int:pk>/', booking_detail, name='booking-detail'),
    path('bookings/<int:pk>/cancel/', booking_cancel, name='booking-cancel'),
    path('admin/bookings/<int:pk>/accept/', admin_accept, name='admin-booking-accept'),
    path('admin/bookings/<int:pk>/refuse/', admin_refuse, name='admin-booking-refuse'),
    path('admin/bookings/<int:pk>/car_taken/', admin_car_taken, name='admin-booking-car-taken'),
    path('admin/bookings/<int:pk>/complete/', admin_complete, name='admin-booking-complete'),
]