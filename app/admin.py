from django.contrib import admin
from .models import (
    Award, Bacteria, Conference, Gallery, Phage, Publication, ResearchProject, Member, Teaching, TextContent,
    Education, ResearchInterest, ActiveResearchProject, PrevResearchProject, ExternalAffiliation
)
from django.utils.html import format_html
from django import forms

class TitleTextareaWidgetMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'title' in self.fields:
            self.fields['title'].widget = forms.Textarea(attrs={'rows': 2, 'cols': 70})

class PublicationInlineForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'
        widgets = {
            'title': forms.Textarea(attrs={'rows': 2, 'cols': 70}),
        }
        
class AwardInlineForm(TitleTextareaWidgetMixin, forms.ModelForm):
    class Meta:
        model = Award
        fields = '__all__'
        
class TeachingInlineForm(TitleTextareaWidgetMixin, forms.ModelForm):
    class Meta:
        model = Teaching
        fields = '__all__'
        
class ConferenceInlineForm(TitleTextareaWidgetMixin, forms.ModelForm):
    class Meta:
        model = Teaching
        fields = '__all__'

class EducationInlineForm(TitleTextareaWidgetMixin, forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class ResearchInterestInlineForm(TitleTextareaWidgetMixin, forms.ModelForm):
    class Meta:
        model = ResearchInterest
        fields = '__all__'

class ActiveResearchProjectInlineForm(TitleTextareaWidgetMixin, forms.ModelForm):
    class Meta:
        model = ActiveResearchProject
        fields = '__all__'

class PrevResearchProjectInlineForm(TitleTextareaWidgetMixin, forms.ModelForm):
    class Meta:
        model = PrevResearchProject
        fields = '__all__'

class ExternalAffiliationInlineForm(TitleTextareaWidgetMixin, forms.ModelForm):
    class Meta:
        model = ExternalAffiliation
        fields = '__all__'

class PublicationInline(admin.TabularInline):
    model = Publication
    form = PublicationInlineForm
    extra = 1
        
class AwardInline(admin.TabularInline):
    model = Award
    form = AwardInlineForm
    extra = 1
        
class TeachingInline(admin.TabularInline):
    model = Teaching
    form = TeachingInlineForm
    extra = 1
    
class ConferenceInline(admin.TabularInline):
    model = Conference
    form = ConferenceInlineForm
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    form = EducationInlineForm
    extra = 1

class ResearchInterestInline(admin.TabularInline):
    model = ResearchInterest
    form = ResearchInterestInlineForm
    extra = 1

class ActiveResearchProjectInline(admin.TabularInline):
    model = ActiveResearchProject
    form = ActiveResearchProjectInlineForm
    extra = 1

class PrevResearchProjectInline(admin.TabularInline):
    model = PrevResearchProject
    form = PrevResearchProjectInlineForm
    extra = 1

class ExternalAffiliationInline(admin.TabularInline):
    model = ExternalAffiliation
    form = ExternalAffiliationInlineForm
    extra = 1

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'designation', 'department', 'university')
    search_fields = ('name', 'category', 'university')
    inlines = [
        EducationInline, ResearchInterestInline, ActiveResearchProjectInline,
        PrevResearchProjectInline, ExternalAffiliationInline, PublicationInline, TeachingInline, AwardInline, ConferenceInline,
    ]
    













@admin.register(ResearchProject)
class ResearchProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date')
    list_editable = ('status','date')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploaded_at', 'thumbnail', 'slider_image')
    list_editable = ('slider_image',)
    list_filter = ('uploaded_at',)  # Filter by upload date
    search_fields = ('title',)  # Search by title

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />',
                obj.image.url
            )
        return "No Image"

    thumbnail.short_description = "Thumbnail"  # Header in the admin panel

@admin.register(TextContent)
class TextContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)

@admin.register(Bacteria)
class BacteriaAdmin(admin.ModelAdmin):
    list_display = ('name', 'strain_category',)
    list_filter = ('strain_category',)
    search_fields = ('name',)
    
@admin.register(Phage)
class PhageAdmin(admin.ModelAdmin):
    list_display = ('name', 'host',)
    search_fields = ('name',)


