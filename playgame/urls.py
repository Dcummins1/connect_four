from django.urls import path
#from playgame.views import join
# from django.contrib import admin
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from connect_four import settings
# from django.conf.urls.static import static

from . import views
#admin.autodiscover()


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('play/', views.Play.as_view(), name='play'),
    #path('play/(?P<game>\d+)/$', join, name='join1'),
    path('joingame/', views.join, name='joingame'),



    path('create/', views.Play.create_game, name='create'),
    #path('games/', views.Games.as_view(), name='games'),

    path('join/', views.join_game_list, name='join'),
    path(r'^joingame/(?P<game_id>[0-9]+)/$', views.Play.as_view(), name='livegame'),

]

# ]+ static(settings.STATIC_URL)
# urlpatterns += staticfiles_urlpatterns()