from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class UserCustom(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.TextField()
    email = models.TextField()
    password = models.TextField()
   
    created_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # Hash password sebelum menyimpan
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
        
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    