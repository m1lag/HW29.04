from django.contrib import admin
from django.urls import path, include

from django.conf.urls import handler404
from app.views import custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),      
    path('news/', include('news.urls')), 
]

handler404 = custom_404 