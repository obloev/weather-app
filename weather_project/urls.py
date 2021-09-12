from weather.views import current, hourly
from django.urls import path

urlpatterns = [
    path('', current, name='current'),
    path('hourly/', hourly, name='hourly'),
    # path('admin/', admin.site.urls),
]
