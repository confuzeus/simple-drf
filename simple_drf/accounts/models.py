from django.contrib.auth.models import AbstractUser
from allauth.account.models import EmailAddress
from django.utils.functional import cached_property


class User(AbstractUser):
    @cached_property
    def primary_email(self):
        email = EmailAddress.objects.get_primary(self)
        if email is None:
            email = self.email
        else:
            email = email.email
        return email

    class Meta:
        ordering = ["-date_joined"]
        db_table = "users"
