from django.db import models
from cases.models import Case

class Document(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')  # uploaded files stored in 'media/documents/'
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
