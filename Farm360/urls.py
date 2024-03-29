from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    SignUpView, ProfileView, EventListView, EventCreateView, EventDeleteView, 
    EventUpdateView, IndexView, EventDetailView, LivestockCreateView, 
    LivestockListView, LivestockDetailView, DashboardView, LivestockUpdateView, 
    LivestockDeleteView, ResourceCreateView, ResourceListView, ResourceDetailView,
    ResourceUpdateView, ResourceDeleteView, TransactionCreateView, TransactionListView, TransactionDetailView, TransactionDeleteView
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
    path('livestock/<int:pk>/edit/', LivestockUpdateView.as_view(), name='livestock_update'),
    path('livestock/<int:pk>/delete/', LivestockDeleteView.as_view(), name='livestock_delete'),

    # resources
    path('add_resource/', ResourceCreateView.as_view(), name='add_resource'),
    path('resource_list/', ResourceListView.as_view(), name='resource_list'),
    path('resource_detail/<int:pk>/', ResourceDetailView.as_view(), name='resource_detail'),
    path('resource/<int:pk>/edit/', ResourceUpdateView.as_view(), name='resource_update'),
    path('resource/<int:pk>/delete/', ResourceDeleteView.as_view(), name='resource_delete'),

    #Transactions
    path('transaction/create/', TransactionCreateView.as_view(), name='create_transaction'),
    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='delete_transaction'),


]


# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
