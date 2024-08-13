from django.urls import path

from . import views

app_name = 'algorithms'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:arg>/', views.arg_test, name='arg_test'),
    path('alg_setup/', views.send_to_alg_setup, name='alg_setup'),
    path('receive_alg_type/', views.receive_alg_type, name='receive_alg_type'),
    path('receive_alg/', views.receive_alg, name='receive_alg'),
    path('send_alg/', views.send_alg, name='send_alg'),
]