from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # path('/', include('djangoapp.urls')),
    path('admin/', admin.site.urls),
    path('', views.index),
    path("django/", include('djangoapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
