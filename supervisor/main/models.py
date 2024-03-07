from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Allocation_File(models.Model):
    Created_at = models.DateTimeField(auto_now_add=True,)
    file_name = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=250)

    
    def __str__(self):
        return str(self.file_name)
    

