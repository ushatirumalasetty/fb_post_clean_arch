from django.db import models

from .post import *

from .user import *


class Comment(models.Model):
    content=models.CharField(max_length=1000)
    commented_at=models.DateTimeField(auto_now=True)
    commented_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_comments")
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='comment',on_delete=models.CASCADE)
