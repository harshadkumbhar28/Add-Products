from django.contrib import admin
from django.urls import path, include
from .views import productsApp, create, show

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', productsApp, name="home"),
    path('create/', create, name="create"),
    path('show/', show, name="show"),
]