from django.db import models

class S_Result(models.Model):
    query = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    link = models.URLField()
    snippet = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title