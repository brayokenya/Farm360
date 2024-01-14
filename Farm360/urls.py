from django.urls import path
from .views import (
    SignUpView, ProfileView, EventListView, EventCreateView, EventDeleteView, 
    EventUpdateView, IndexView, EventDetailView, LivestockCreateView, 
    LivestockListView, LivestockDetailView, DashboardView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='home'), 
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path('profile/', ProfileView.as_view(), name='profile'),
    # events
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_details'),
    path('create_event/', EventCreateView.as_view(), name='create_event'),
    path('event_list/', EventListView.as_view(), name='event_list'), 
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path("event/<int:pk>/update/", EventUpdateView.as_view(), name="update_event"),
    # livestock
    path('create_livestock/', LivestockCreateView.as_view(), name='create_livestock'),
    path('livestock_list/', LivestockListView.as_view(), name='livestock_list'),
    path('livestock_detail/<int:pk>/', LivestockDetailView.as_view(), name='livestock_detail'),
]
