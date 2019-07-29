from .models import Blog, Category
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import BlogForm

# Create your views here.
def index(request):
    blogs = Blog.objects
    return render(request, 'index.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog' : blog_detail})

def info(request):
    return render(request, 'info.html')

def new(request):
    form = BlogForm(request.POST)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/detail/'+str(blog.id))
    else:
        form = BlogForm()
    return render(request, 'new.html', {'form' : form})