
from django.contrib import admin
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('chart/', include('core.urls'))

    # path('api/data/', get_data, name='api-data'),
    # path('api/chart/data', ChartData.as_view())
]
