from django.contrib import admin
from django.urls import path
from . import views as local_views
from posts import views as posts_views
from users import views as users_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', local_views.home, name = 'home'),
    path('admin/', admin.site.urls, name = 'admin_site'),
    path('hello-world/',local_views.hello_world, name = 'hello_world'),
    path('ordering/',local_views.ordering, name='sort'),
    path('access/<str:name>/<int:age>',local_views.access, name = 'access'),
    path('posts/',posts_views.posts, name = 'posts'),
    path('login/',users_views.login_view, name = 'login'),
    path('logout/',users_views.logout_view, name='logout'),
    path('sign_up/',users_views.sign_up_view, name='sign_up'),
    path('edit_user/',users_views.edit_user, name='edit_user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
