from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from .models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    default_error_messages = {
        'inactive_account': _('User account is disabled.'),
        'invalid_credentials': _('Unable to login with provided credentials.')
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = authenticate(
            email=attrs.get("email"), password=attrs.get('password')
            )
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(
                    self.error_messages['inactive_account']
                    )
            return attrs
        else:
            raise serializers.ValidationError(
                self.error_messages['invalid_credentials']
                )


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ("auth_token", "created", "user")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'email', 'first_name', 'last_name',)
        model = User
