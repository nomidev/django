from django.db import models

# Create your models here.
class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback from {self.user_name} ({self.user_email})'