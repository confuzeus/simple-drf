from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from simple_drf.accounts.models import User


class UserSerializer(serializers.ModelSerializer[User]):
    email = serializers.SerializerMethodField()

    def get_email(self, instance):
        return instance.primary_email

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "date_joined", "email"]
        read_only_fields = ["id", "date_joined"]


class UserDeleteSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)

    def validate_password(self, value):
        if not self.context["user"].check_password(value):
            raise serializers.ValidationError("Wrong password!")
        return value

    def destroy(self):
        self.context["user"].delete()
