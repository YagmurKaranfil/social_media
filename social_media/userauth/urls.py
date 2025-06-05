from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginn, name='login'),    # URL /login/ olarak kalacak
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutt, name='logout'), # /logout/ olacak
    path('upload/', views.upload, name='upload'),
    path('like-post/<str:id>/', views.likes, name='like-post'),
    path('post/<str:id>/', views.home_post, name='home-post'),
    path('explore/', views.explore, name='explore'),
    path('profile/<str:id_user>/', views.profile, name='profile'),
    path('search-results/', views.search_results, name='search_results'),
    path('follow/', views.follow, name='follow'),
    path('delete/<str:id>', views.delete, name='delete'),
]
