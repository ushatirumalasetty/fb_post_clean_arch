from django.db import models

from .user import *

from .post import *

from .comment import *

from django.contrib.auth.models import AbstractUser

class Reaction(AbstractUS):
    REACTIONS=(
        ("WOW","wow"),
        ("LIT","lit"),
        ("LOVE","love"),
        ("HAHA","haha"),
        ("THUMBS-UP","thumps_up"),
        ("THUMBS-DOWN","thumps_down"),
        ("ANGRY","angry"),
        ("SAD","sad")
        )
    post=models.ForeignKey(Post,null=True,on_delete=models.CASCADE,related_name="reaction")
    comment=models.ForeignKey(Comment,null=True,on_delete=models.CASCADE,related_name="reaction")
    reaction=models.CharField(max_length=100,choices=REACTIONS)
    reacted_at=models.DateTimeField(auto_now=True)
    reacted_by=models.ForeignKey(User,on_delete=models.CASCADE)
