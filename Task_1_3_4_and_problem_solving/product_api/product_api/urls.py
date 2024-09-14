from django.contrib import admin
from django.urls import path, include
from users.views import api_root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api/user/', include('users.urls')),
    path('', api_root, name='api-root'),
]
