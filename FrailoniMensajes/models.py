from django.db import models



# Create your models here.
class Chat (models.Model):
    mensaje=models.CharField(max_length=500)
    
    def __str__(self):
        return self.mensaje 