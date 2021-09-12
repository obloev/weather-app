from weather.views import current
from django.urls import path

urlpatterns = [
    path('', current, name='current'),
    # path('admin/', admin.site.urls),
]
