from django.urls import path

from . import views

urlpatterns=[	
	path(
		route='<str:username>',
		view=views.UserDetailView.as_view(),
		name='detail'
	),

    path(
    	route='login/',
    	view=views.login_view,
    	name = 'login'
    	),
    path(
    	route='logout/',
    	view=views.logout_view,
    	name='logout'
    	),
    path(
    	route='sign_up/',
    	view=views.sign_up_view,
    	name='sign_up'
    	),
    path(
    	route='edit_user/',
    	view=views.edit_user,
    	name='edit_user'
    	),
]