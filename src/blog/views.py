from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.http import Http404


# Create your views here.


def blog_post_detail_page(request, slug):
    queryset = BlogPost.objects.filter(slug=slug)
    
    if queryset.count() >= 1:
        obj = queryset.first()
    else:
        raise Http404
        
    template_name = "blog/blog_post_detail_page.html"
    context = { "object" : obj }
    return render(request, template_name, context)