from django.urls import path

from simple_drf.accounts.api import views

app_name = "accounts_api"

urlpatterns = [path("", views.UserView.as_view(), name="user-detail")]
