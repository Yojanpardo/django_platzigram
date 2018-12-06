from django.urls import path

from . import views

urlpatterns=[
    path(
        route='post_detail/<int:id>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
    path(
    	route='',
    	view=views.PostsView.as_view(),
    	name='posts'
    	),
    path(
    	route='create_post/',
    	view=views.create_post,
    	name='create_post'
    	),
]