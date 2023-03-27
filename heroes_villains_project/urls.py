
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/supers/', include('supers.urls')),
    path('api/super_types/', include('super_types.urls'))
]
