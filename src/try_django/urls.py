"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
#import blog
from try_django import views
from blog.views import (
    blog_post_create_view,
    )
from searches.views import (
    search_view,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('about/', views.about_page),
    path('contact/', views.contact_page),
    path('example/', views.example_get_template),

    path("login/", views.contact_page),

    path("blog/", include("blog.urls")),

    # path("blog/<slug>/", blog_post_detail_page),
    # path("blog/<slug>/edit/", blog_post_update_view),
    # path("blog/<slug>/delete/", blog_post_delete_view),
    # path("blog/", blog_post_list_view),
    path("blog-new/", blog_post_create_view),
    path("search/", search_view),


]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)