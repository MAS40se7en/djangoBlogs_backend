from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('update_user/', views.updateUser, name='update_user'),
    path('create_blog/', views.createBlog, name='create_blog'),
    path('list_blogs/', views.listBlogs, name='list_blogs'),
    path('blogs/<slug:slug>/', views.get_blog, name='get_blog'),
    path('update_blog/<int:pk>/', views.updateBlog, name='update_blog'),
    path('delete_blog/<int:pk>/', views.deleteBlog, name='delete_blog'),
    path("get_username/", views.get_username, name="get_username"),
    path("get_userinfo/<str:username>/", views.get_userinfo, name="get_userinfo"),
    path("get_user/<str:email>/", views.get_user, name="get_user")
]