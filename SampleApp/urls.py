from django.urls import path
from .views import SignUpView, ProfileView, CollectionListView, CollectionDetailView, SampleCreateView, CollectionCreateView,CollectionDeleteView, SampleDeleteView, CollectionUpdateView, SampleUpdateView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', CollectionListView.as_view(), name='home'),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('collection/<int:pk>/', CollectionDetailView.as_view(), name='collection_details'),
    path('collection/<int:collection_id>/add_sample/', SampleCreateView.as_view(), name='add_sample'),
    path('create_collection/', CollectionCreateView.as_view(), name='create_collection'),
    path('collection/<int:pk>/delete/', CollectionDeleteView.as_view(), name='collection_delete'),
    path('sample/<int:pk>/delete/', SampleDeleteView.as_view(), name='sample_delete'),
    path("collections/<int:pk>/update/", CollectionUpdateView.as_view(), name="update_collection"),
    path("samples/<int:pk>/update/", SampleUpdateView.as_view(), name="update_sample"),
]
