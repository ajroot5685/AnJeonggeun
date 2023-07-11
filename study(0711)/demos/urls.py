from django.urls import path
from .views import index, calculator

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('test/', index),
    path('cal/', calculator),
]
