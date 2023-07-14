from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('games/', include('content.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('messaging/', include('messaging.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
