from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(upload_to='pic', null= True)
    created_on = models.DateTimeField(auto_now_add=True , null= True)

    def __str__(self):
        return self.title