from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost



def home_page(request):
    qs = BlogPost.objects.all()[0:5]
    print(qs)
    context = {"title":"Welcome to MongoBlogo","blog_list" : qs}
    return render(request, "home.html", context )

def about_page(request):
    return render(request, "hello_world.html", {"title":"About us"})

def contact_page(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title":"Contct us",
        "form" : form
    }
    return render(request, "form.html", context)


def example_get_template(request):
    context         = {"title":"Example from views.py"}
    template_name   = "hello_world.html"
    template_obj    = get_template(template_name)
    
    return HttpResponse(template_obj.render(context))