from django.urls import path
from .views import home, post_detail, create_post, update_post, delete_post, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('create/', create_post, name='create_post'),
    path('update/<int:id>/', update_post, name='update_post'),
    path('delete/<int:id>/', delete_post, name='delete_post'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]