from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.generic import TemplateView

from simple_drf.core import views as core_views

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("up/", core_views.healthcheck, name="healthcheck"),
    path("accounts/", include("allauth.urls")),
    path("_allauth/", include("allauth.headless.urls")),
    path("_drf/", include("rest_framework.urls")),
    path("api/accounts/", include("simple_drf.accounts.api.urls")),
    path(
        "",
        login_required(TemplateView.as_view(template_name="pages/home.html")),
        name="home",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
