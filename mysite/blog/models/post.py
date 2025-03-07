
from django.db import models
from django.contrib.auth.models import User

class Post (models.Model):
    nome = models.CharField(max_length=100)
    email = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nome