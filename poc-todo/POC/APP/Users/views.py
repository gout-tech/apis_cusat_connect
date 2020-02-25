from rest_framework.generics import (
    GenericAPIView, CreateAPIView, ListAPIView,
    RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import (
    UserLoginSerializer, TokenSerializer, UserSerializer
)
from rest_framework import status
from .models import User, ExpiringToken


class UserLoginAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            token, _ = ExpiringToken.objects.get_or_create(user=user)
            if user:
                if token.expired():
                    token.delete()
                    return Response(data="Token expired, Login again",
                                    status=status.HTTP_401_UNAUTHORIZED
                                    )
                else:
                    return Response(
                        data=TokenSerializer(token).data,
                        status=status.HTTP_200_OK,
                    )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_401_UNAUTHORIZED,
            )


class UserCreationAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class UserListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


class UserUpdateView(RetrieveUpdateAPIView):
    permission_classes = ()
    serializer_class = UserSerializer

    def get_object(self):
        queryset = User.objects.get(pk=self.kwargs.get('pk'))
        return queryset

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        data = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)


class UserDeleteView(RetrieveDestroyAPIView):
    permission_classes = ()
    serializer_class = UserSerializer

    def get_object(self):
        queryset = User.objects.get(pk=self.kwargs.get('pk'))
        return queryset

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.destroy(serializer)
        return Response("Deleted", status=status.HTTP_200_OK)


class GetUserView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        queryset = User.objects.get(pk=self.kwargs.get('pk'))
        return queryset
