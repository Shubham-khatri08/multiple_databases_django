from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    class Meta:
        app_label = 'user'

    def __str__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey('User', related_name='user', on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'user'

    def __str__(self):
        return self.user