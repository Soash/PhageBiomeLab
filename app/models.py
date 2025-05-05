from django.db import models

class ResearchProject(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='research_project_images/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')

    def __str__(self):
        return self.title
    
class Member(models.Model):
    # Choices for the category field
    CATEGORY_CHOICES = [
        ('lab_investigator', 'Principal Investigator'),
        ('lab_investigator_co', 'Coinvestigator'),
        ('ms_thesis_student', 'MS (Thesis) Student'),
        ('undergraduate_student', 'Undergraduate Student'),
        ('alumni', 'Alumni'),
    ]

    # Model fields
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='members/photos/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='gallery_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"
    
class TextContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Bacteria(models.Model):
    STRAIN_CATEGORY_CHOICES = [
        ('clinical', 'Clinical'),
        ('reference', 'Reference'),
        ('laboratory', 'Laboratory'),
    ]

    name = models.CharField(max_length=100)
    amr_status = models.CharField(max_length=100)
    strain_category = models.CharField(max_length=20, choices=STRAIN_CATEGORY_CHOICES)
    source = models.CharField(max_length=255, verbose_name="Source")
    active_date = models.DateField()

    def __str__(self):
        return self.name

class Phage(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    information = models.TextField()

    def __str__(self):
        return self.name

