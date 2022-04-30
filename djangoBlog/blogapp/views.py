from django.http import Http404
from django.shortcuts import render
from .models import Posts
from .forms import CommentForm

def index(request):
    all_posts = Posts.objects.all()
    return render(request, 'index.html', {'posts': all_posts})

def detail(request, slug):
    try:
       post_details = Posts.objects.get(slug=slug)
       
       if request.method == "POST":
          form = CommentForm(request.POST)

          if form.is_valid:
             comment = form.save(commit=False)
             comment.post = request.post
             comment.save()

       else:
         form = CommentForm() 
 
       return render(request, 'detail.html', {'details': post_details})

    except Posts.DoesNotExist:
       raise Http404("Can not find such a page")    