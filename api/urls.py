
from timeit import repeat
from django.urls import path, re_path
from django.conf.urls import include
from .views import BitiruvchiListView, BitiruvchiView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('list', BitiruvchiView)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    # path('', BitiruvchiListView.as_view(), name="BAPI")
] 