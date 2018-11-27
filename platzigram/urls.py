from django.contrib import admin
from django.urls import path
from . import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/',local_views.hello_world),
    path('ordering/',local_views.ordering),
    path('access/<str:name>/<int:age>',local_views.access),
    path('posts/',posts_views.posts),
]
