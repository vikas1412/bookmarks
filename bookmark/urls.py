from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmarks/', include('homepage.urls')),

    path('', RedirectView.as_view(url="bookmarks/", permanent=True)),
]
