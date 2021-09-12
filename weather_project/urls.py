from weather.views import current, hourly, daily
from django.urls import path

urlpatterns = [
    path('', current, name='current'),
    path('hourly/', hourly, name='hourly'),
    path('daily/', daily, name='daily'),
    # path('admin/', admin.site.urls),
]
