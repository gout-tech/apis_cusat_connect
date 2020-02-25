from django.urls import include, path
from django.contrib import admin


api_urls = [

    path('', include('APP.Users.urls')),
    path('', include('APP.Task.urls')),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
