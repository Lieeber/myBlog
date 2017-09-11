from django.contrib import admin

# Register your models here.
from comments.models import Comment


class CommentDetail(admin.ModelAdmin):
    # name = models.CharField(max_length=100)
    # email = models.EmailField(max_length=255)
    # url = models.URLField(blank=True)
    # text = models.TextField()
    # created_time = models.DateTimeField(auto_now_add=True)
    # post = models.ForeignKey('blog.Post')
    list_display = ['name', 'created_time', 'text']


admin.site.register(Comment, CommentDetail)
