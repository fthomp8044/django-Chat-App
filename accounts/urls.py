from django.urls import path
from . import views

# dont forget the app_name. it helps refer to the name for url
app_name= 'accounts'

urlpatterns = [
    path('<int:pk>/profile/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/', views.ProfileCreateView.as_view(), name='profile'),
    path('signup/', views.SignUpView.as_view(), name='signup'),



]
