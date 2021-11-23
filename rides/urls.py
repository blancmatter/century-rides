from django.urls import path
from .views import HomeView, RidesView, RideDetailView, AddRideView, UpdateRideView, DeleteRideView, DuplicateRideView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Old non-classed based view path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('ride/', RidesView.as_view(), name='rides'),
    path('ride/<int:pk>', RideDetailView.as_view(), name='ride-details'),
    path('add_ride/', AddRideView.as_view(), name='add-ride'),
    path('ride/edit/<int:pk>', UpdateRideView.as_view(), name='update-ride'),
    path('ride/<int:pk>/remove', DeleteRideView.as_view(), name='delete-ride'),
    path('ride/<int:pk>/copy', DuplicateRideView.as_view(), name='copy-ride')
]

urlpatterns += staticfiles_urlpatterns()
