


from django.urls import path,include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('upload-image',views.PhotoImageView)

urlpatterns = [
    path('all-images/',views.allImages,name="all-images"),
    path('image-result/<str:pk>/',views.imageResult,name="image-result"),
    path('',include(router.urls))
]
