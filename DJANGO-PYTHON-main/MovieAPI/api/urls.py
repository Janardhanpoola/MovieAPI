from django.urls import path,include

from . import views


urlpatterns = [
    path('movieapi/',views.MovieAPIView.as_view(),name='movieapi'),
    path('movieapi/<int:id>/',views.MovieAPIDetail.as_view(),name='movieidapi')
]