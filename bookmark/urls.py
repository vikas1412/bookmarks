from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmarks/', include('homepage.urls')),

    path('', RedirectView.as_view(url="bookmarks/", permanent=True)),

    path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
