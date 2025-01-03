from rest_framework import serializers

from simple_drf.accounts.models import User


class UserSerializer(serializers.ModelSerializer[User]):
    email = serializers.SerializerMethodField()

    def get_email(self, instance):
        return instance.primary_email

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "date_joined", "email"]
        read_only_fields = ["id", "date_joined"]
