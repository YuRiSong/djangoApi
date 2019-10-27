
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mystorage import views

# django rest framework -> router -> url

router = DefaultRouter()
router.register('essay', views.PostViewSet)
router.register('album', views.ImgViewSet)
router.register('files', views.FileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
