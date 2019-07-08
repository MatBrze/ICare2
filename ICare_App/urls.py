from django.urls import path
from ICare_App import views

app_name = 'ICare_App'

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('donate/', views.DonateView.as_view(), name='donate'),
]