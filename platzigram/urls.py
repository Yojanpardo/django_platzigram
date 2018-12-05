from django.contrib import admin
from django.urls import path, include
from . import views as local_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin_site'),
    path('hello-world/',local_views.hello_world, name = 'hello_world'),
    path('ordering/',local_views.ordering, name='sort'),
    path('access/<str:name>/<int:age>',local_views.access, name = 'access'),
    path('welcome/',local_views.home,name='welcome'),

    path('',include(('posts.urls','posts'),namespace='posts')),
    path('users/',include(('users.urls','users'),namespace='users')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
