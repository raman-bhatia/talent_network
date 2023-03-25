from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('submit/', views.submit_activity, name='submit_activity'),
    # ex: /polls/5/
    path('<int:activity_id>/search/', views.search_activities, name='search'),
    # ex: /polls/5/vote/
    path('<int:activity_id>/dashboard/', views.dashboard_activity, name='dashboard'),
]