from django.urls import path
from .views import (
    TaskCreationAPIView, TaskUpdateView, TaskListView,
    TaskListAllView, TaskFilterView, TaskDeleteView
)

app_name = 'APP.Task'

urlpatterns = [

    path('users/task-creation/', TaskCreationAPIView.as_view(), name="task-creation"),
    path('users/task-update/<int:pk>/', TaskUpdateView.as_view(), name="task-update"),
    path('users/task-delete/<int:pk>/', TaskDeleteView.as_view(), name="task-delete"),
    path('users/task-view/<int:pk>/', TaskListView.as_view(), name="task-view"),
    path('users/task-filter/', TaskFilterView.as_view(), name="task-filter"),
    path('users/task-list-all/', TaskListAllView.as_view(), name="task-list-all"),

]
