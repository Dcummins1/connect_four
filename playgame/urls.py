from django.urls import path
# from django.contrib import admin
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from connect_four import settings
# from django.conf.urls.static import static

from . import views
#admin.autodiscover()


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('play/', views.Play.as_view(), name='play'),]

# ]+ static(settings.STATIC_URL)
# urlpatterns += staticfiles_urlpatterns()