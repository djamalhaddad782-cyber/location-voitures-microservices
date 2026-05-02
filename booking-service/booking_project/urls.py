"""
URL configuration for booking_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from bookings.views import BookingViewSet, AdminBookingViewSet

# Instanciation des vues
booking_list = BookingViewSet.as_view({'get': 'list', 'post': 'create'})
booking_detail = BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
booking_cancel = BookingViewSet.as_view({'post': 'cancel'})

admin_accept = AdminBookingViewSet.as_view({'patch': 'accept'})
admin_refuse = AdminBookingViewSet.as_view({'patch': 'refuse'})
admin_car_taken = AdminBookingViewSet.as_view({'patch': 'car_taken'})
admin_complete = AdminBookingViewSet.as_view({'patch': 'complete'})

urlpatterns = [
    path('health/', lambda request: JsonResponse({'status': 'ok'})),
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/bookings/', booking_list, name='booking-list'),
    path('api/bookings/<int:pk>/', booking_detail, name='booking-detail'),
    path('api/bookings/<int:pk>/cancel/', booking_cancel, name='booking-cancel'),
    
    path('api/admin/bookings/<int:pk>/accept/', admin_accept, name='admin-booking-accept'),
    path('api/admin/bookings/<int:pk>/refuse/', admin_refuse, name='admin-booking-refuse'),
    path('api/admin/bookings/<int:pk>/car_taken/', admin_car_taken, name='admin-booking-car-taken'),
    path('api/admin/bookings/<int:pk>/complete/', admin_complete, name='admin-booking-complete'),
]