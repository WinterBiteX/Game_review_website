from django.urls import path
from WebApp import views

urlpatterns = [
    path("home_page/",views.home_page,name="home_page"),
    path("game_page/",views.game_page,name="game_page"),
    path("game_details/<int:game_id>/",views.game_details,name="game_details"),
    path("game_trailer/<int:game_id>/",views.game_trailer,name="game_trailer"),
    path('search/', views.search, name='search'),
    path('search_game/', views.search_games, name='search_game'),
    path('game_filter/<game_name>/',views.game_filter,name='game_filter'),
    path('contact/',views.contact,name='contact'),
    path('login_page/',views.login_page,name='login_page'),
    path('save_contact/',views.save_contact,name='save_contact'),
    path('',views.user_login,name="user_login"),
    path('save_user/',views.save_user_details,name="save_user"),
    path('login_user/',views.login_user,name="login_user"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('upcoming_details/<int:up_id>/',views.upcoming_details,name="upcoming_details"),
    path('upcoming_trailer/<int:up_id>/',views.upcoming_trailer,name="upcoming_trailer"),
    path("save_comment/",views.save_comment,name="save_comment"),
    path("toggle_favorite/<int:game_id>/",views.toggle_favorite,name="toggle_favorite"),
    path("favorite/",views.favorite,name="favorite"),
    path('remove_favorite/<int:favorite_id>/', views.remove_favorite, name='remove_favorite'),
    path('fav_save_comment/', views.fav_save_comment, name='fav_save_comment'),
    path("blog_post/",views.blog_post,name="blog_post"),
    path("save_blog_post/",views.save_blog,name="save_blog_post")
]
