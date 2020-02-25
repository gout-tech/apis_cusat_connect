from django.urls import path
from .views import (
    UserLoginAPIView, UserCreationAPIView, UserListView, UserUpdateView,
    UserDeleteView, GetUserView
)

app_name = 'APP.User'

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name="login"),
    path('users/user-creation/', UserCreationAPIView.as_view(), name="user-creation"),
    path('users/user-list/', UserListView.as_view(), name="user-list"),
    path('users/user-update/<int:pk>', UserUpdateView.as_view(), name="user-update"),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name="user-delete"),
    path('users/user-view/<int:pk>/', GetUserView.as_view(), name="user-view"),

]
