from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    desc= models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #date = models.DateField(auto_now_add=True)
    #created_at = models.DateTimeField(auto_now_add=True )
    # updated_at=models.DateTimeField(au to_now_add=True,auto_now=False)
    
    
    def __str__(self):
        return self.title
    


