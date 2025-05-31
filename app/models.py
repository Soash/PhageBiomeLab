from django.db import models
from tinymce.models import HTMLField

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
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Member(models.Model):
    # Choices for the category field
    CATEGORY_CHOICES = [
        ('lab_investigator', 'Principal Investigator'),
        ('lab_investigator_co', 'Coinvestigator'),
        ('phd_student', 'PhD Student'),
        ('ms_thesis_student', 'MS (Thesis) Student'),
        ('undergraduate_student', 'Undergraduate Student'),
        ('alumni', 'Alumni'),
    ]

    # Model fields
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='members/photos/', blank=True, null=True)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    biography = HTMLField(blank=True, null=True)
    
    # education = HTMLField(blank=True, null=True)
    # research_interests = HTMLField(blank=True, null=True)
    # active_research_project = HTMLField(blank=True, null=True)
    # previous_research_project = HTMLField(blank=True, null=True)
    
    # journal_publications = HTMLField(blank=True, null=True)
    # external_affiliations = HTMLField(blank=True, null=True)
    graduate_supervision = HTMLField(blank=True, null=True)
    

    def __str__(self):
        return self.name


class Publication(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='publications')
    title = models.TextField(max_length=200, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    
class Award(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='awards')
    title = models.TextField(max_length=200, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    
class Teaching(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='teachings')
    title = models.TextField(max_length=200, blank=True, null=True)
    position = models.PositiveIntegerField(blank=True, null=True)
    
class Conference(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='conferences')
    title = models.TextField(max_length=200, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    
class Education(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='educations')
    title = models.TextField(max_length=200, blank=True, null=True)
    position = models.PositiveIntegerField(blank=True, null=True)
    
class ResearchInterest(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='research_interests')
    title = models.TextField(max_length=200, blank=True, null=True)
    position = models.PositiveIntegerField(blank=True, null=True)
    
class ActiveResearchProject(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='active_research_projects')
    title = models.TextField(max_length=200, blank=True, null=True)
    position = models.PositiveIntegerField(blank=True, null=True)
    
class PrevResearchProject(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='prev_research_projects')
    title = models.TextField(max_length=200, blank=True, null=True)
    position = models.PositiveIntegerField(blank=True, null=True)
    
class ExternalAffiliation(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='external_affiliations')
    title = models.TextField(max_length=200, blank=True, null=True)
    position = models.PositiveIntegerField(blank=True, null=True)














    
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

