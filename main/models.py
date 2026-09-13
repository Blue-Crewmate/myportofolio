import uuid
from django.db import models

# Create your models here.
class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title

    @property
    def contain_photo(self):
        return self.thumbnail != None
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Project(models.Model):
    PROJECT_STATUS = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    collaborators = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=PROJECT_STATUS, default='completed')
    def __str__(self):
        return self.title

    @property
    def contain_photo(self):
        return self.thumbnail != None
    
    @property
    def is_ongoing(self):
        return self.status == 'ongoing'

class Music(models.Model):
    GENRE_CHOICES = [
            ('pop', 'Pop'),
            ('rock', 'Rock'),
            ('jazz', 'Jazz'),
            ('funk', 'Funk'),
            ('classical', 'Classical'),
            ('swing', 'Swing'),
        ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='pop')
    audio = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.title

    @property
    def contain_audio(self):
        return self.audio != None