from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField("제목", max_length = 200)
    slug = models.SlugField("주소키", unique = True)
    description = models.CharField("설명", max_length=200, blank=True)
    content = models.TextField("본문")
    create_date = models.DateTimeField("작성시각", auto_now_add = True)
    modify_date = models.DateTimeField("수정시각", auto_now = True)
    published_date = models.DateTimeField("게시시각", blank = True, null = True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    