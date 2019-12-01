from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('list/',views.blog_list,name='blog_list'),
	path('item/<int:blog_id>',views.blog_item,name='blog_item'),
	path('post/',views.blog_post,name='blog_post'),
	path('post/submit/',views.blog_post_submit,name='blog_post_submit'),
	path('edit/<int:blog_id>',views.blog_edit,name='blog_edit'),
	path('update/<int:blog_id>',views.blog_update,name='blog_update'),
	path('delete/<int:blog_id>',views.blog_delete,name='blog_delete'),
]