from django.db import models
from django.conf import settings

class Media(models.Model):
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]   
    MEDIA_CATEGORY = [
        ('gallery', 'Gallery'),
        ('profile', 'Profile'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='media')
    #file = models.FileField(upload_to='media/')  # Stores images/videos
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    media_category = models.CharField(max_length=10, choices=MEDIA_TYPES)
    media_url = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.media_type} - {self.file.name}"
    
    
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(blank=True, null=True) 
    media = models.ManyToManyField(Media, blank=True)  # A post can have multiple media files
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.email} on {self.created_at}"