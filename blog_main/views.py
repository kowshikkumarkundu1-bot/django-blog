from django.shortcuts import render
from blog.models import Category,Blog

def home(request):
    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True)
    context = {
        'categories':categories,
        'featured_post': featured_post
    }
    return render(request,'home.html',context)