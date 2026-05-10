from django.urls import path
from .views import (
    home,
    post_detail,
    create_post,
    update_post,
    delete_post,
    register
)

# Django auth (login/logout)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 🏠 HOME
    path('', home, name='home'),

    # 📄 POST DETAIL
    path('post/<int:id>/', post_detail, name='post_detail'),

    # ➕ CREATE
    path('create/', create_post, name='create_post'),

    # ✏️ UPDATE
    path('update/<int:id>/', update_post, name='update_post'),

    # ❌ DELETE
    path('delete/<int:id>/', delete_post, name='delete_post'),

    # 🔐 AUTH
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]