from django.db import models

# Create your models here.
class Register(models.Model):
    roll_number = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username

class PdfUpload(models.Model):
    branch = models.CharField(max_length=20)
    regulation = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    file_path = models.FileField(upload_to='pdfs/',max_length=200)
    file_name = models.CharField(max_length=100)
    uploaded_by = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject + ' uploaded by ' + self.uploaded_by