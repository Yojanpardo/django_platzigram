from django.contrib import admin
from django.urls import path
from . import views as local_views
from posts import views as posts_views
from users import views as users_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/',local_views.hello_world),
    path('ordering/',local_views.ordering),
    path('access/<str:name>/<int:age>',local_views.access),
    path('posts/',posts_views.posts),
    path('login/',users_views.login_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
