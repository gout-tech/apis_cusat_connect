from rest_framework.generics import (
     CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView,
     ListAPIView, RetrieveDestroyAPIView
)
from rest_framework.response import Response
from .serailizers import TaskGetSerializer, UserSerializer
from rest_framework import status
from .models import UserTasks
from APP.Users.models import User


class TaskCreationAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = TaskGetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class TaskUpdateView(RetrieveUpdateAPIView):

    permission_classes = ()
    serializer_class = TaskGetSerializer

    def get_object(self):
        queryset = UserTasks.objects.get(pk=self.kwargs.get('pk'))
        return queryset

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        data = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)


class TaskListView(RetrieveAPIView):
    permission_classes = ()
    serializer_class = TaskGetSerializer

    def get_object(self):
        queryset = UserTasks.objects.get(pk=self.kwargs.get('pk'))
        return queryset


class TaskListAllView(ListAPIView):
    permission_classes = ()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


class TaskFilterView(ListAPIView):
    permission_classes = ()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(id=self.request.GET.get("user_id"))
        return queryset


class TaskDeleteView(RetrieveDestroyAPIView):
    permission_classes = ()
    serializer_class = TaskGetSerializer

    def get_object(self):
        queryset = UserTasks.objects.get(pk=self.kwargs.get('pk'))
        return queryset

    def perform_destroy(self, instance):
        instance.delete()
