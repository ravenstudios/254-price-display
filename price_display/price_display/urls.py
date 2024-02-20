from django.contrib import admin
from django.urls import path, include


app_name = 'display_app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('display_app/', include('display_app.urls')),
    # path('finances/', include('finances.urls')),
    # path('', views.index, name='index'),
    # path('display', views.display, name='display'),
]
