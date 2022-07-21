from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about/',views.about, name='about'),
     path('racquets/',views.racquets_index, name='index'),
     path('racquets/<int:racquet_id>/',views.racquets_detail, name='detail'),
     path('racquets/create/', views.RacquetCreate.as_view(), name='racquets_create'),
     path('racquets/<int:pk>/update/', views.RacquetUpdate.as_view(), name='racquets_update'),
     path('racquets/<int:pk>/delete/', views.RacquetDelete.as_view(), name='racquets_delete'),
     path('racquets/<int:racquet_id>/add_restring/', views.add_restring, name='add_restring'),
]