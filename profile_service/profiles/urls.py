from django.urls import path
from .views import ProfileListCreateView, ProfileDetailView

urlpatterns = [
    path('', ProfileListCreateView.as_view(), name='profile-list-create'),  # Список профилей и создание
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),  # Просмотр и редактирование профиля
]
