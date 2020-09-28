from django.urls import path
from blog import views

urlpatterns = [
    path("<slug>/", views.blog_post_detail_page),
    path("<slug>/edit/", views.blog_post_update_view),
    path("<slug>/delete/", views.blog_post_delete_view),
    path("", views.blog_post_list_view),
    #path("blog-new/", views.blog_post_create_view),
]