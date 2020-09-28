from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.http import Http404
from .forms import BlogPOstModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.



def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = "blog/list.html"
    context = {"object_list":qs}
    return render(request , template_name , context)

@staff_member_required
def blog_post_create_view(request):
    template_name = "blog/create.html"
    form = BlogPOstModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPOstModelForm()
        return redirect("/blog/")
    context = {"form":form}
    return render(request , template_name , context)

def blog_post_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug) 
    template_name = "blog/detail.html"
    context = {"object":obj}
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPOstModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/blog/")
    template_name = "form.html"
    context = {"form":form, "title":f"updating {obj.title}"}
    return render(request , template_name , context)

@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    if request.method == "POST":
        obj.delete()
        return redirect("/blog/")
    context = {"object":obj}
    return render(request , template_name , context)
