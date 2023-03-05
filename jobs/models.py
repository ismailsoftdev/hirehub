from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Job(models.Model):
    JOB_TYPES = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
        ('Remote', 'Remote'),
        ('Volunteer', 'Volunteer'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    description = RichTextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100, choices=JOB_TYPES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job.title + ' - ' + self.applicant.username
