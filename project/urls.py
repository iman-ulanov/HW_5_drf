from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app import views

router = routers.DefaultRouter()
router.register('mentor', views.MentorViewSet)
router.register('course', views.CourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/', views.StudentCreateListView.as_view()),
    path('api/student/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),
    path('api/v-1.0/', include(router.urls)),
]
