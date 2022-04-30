from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    intro = models.TextField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    

class Comments(models.Model):
    post = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
