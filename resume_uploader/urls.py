from api import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume/', views.ProfileView.as_view(), name='resume'),
    path('list/', views.ProfileView.as_view(), name='list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)