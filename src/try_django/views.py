from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    context = {"list_a" : [1,2,3,4,5]}
    return render(request, "home.html", context )

def about_page(request):
    return render(request, "hello_world.html", )

def contact_page(request):
    return render(request, "hello_world.html", )

def example_get_template(request):
    context         = {"title":"Example from views.py"}
    template_name   = "hello_world.html"
    template_obj    = get_template(template_name)
    
    return HttpResponse(template_obj.render(context))