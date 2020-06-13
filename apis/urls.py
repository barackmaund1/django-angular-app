from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import GenericAPIView,TutorialViewSet
router=DefaultRouter()
router.register('tutorial',TutorialViewSet,basename='tutorial')
urlpatterns = [
    path('api/tutorials/', views.tutorial_list),
    path('api/tutorials/<int:pk>/', views.tutorial_detail),
    path('api/tutorials/published/', views.tutorial_list_published),
    path('generic/tutorial/<int:id>/',GenericAPIView.as_view()),
    path('',include(router.urls))
]