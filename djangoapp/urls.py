from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path("home/", views.index, name="Home"),
    path('about/', views.about , name="About"),
    path('contact/', views.contact, name="Contact"),

    # path for contact us view

    # path for registration

    # path for login

    # path for logout

    # path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)