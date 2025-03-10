
from django.urls import path
from app import views

urlpatterns = [
    path('', views.view_test, name='home'),
    path('<int:id>',views.chart_view, name="chart"),
    path('search/',views.search_view, name='search_element')
    
]
