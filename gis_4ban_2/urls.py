from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),

    path('subscribe/', include('subscribeapp.urls')),
    path('likes/', include('likeapp.urls')),
]