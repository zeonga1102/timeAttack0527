from django.db import models
import hashlib

# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table = "user"

    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)

    def __init__(self, email, password):
        self.email = email
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
