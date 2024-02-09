
from django.contrib import admin
from django.urls import path, include

app_name = 'config'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('accounts.urls'))
]
