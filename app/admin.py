from django.contrib import admin
from .models import Bacteria, Gallery, Phage, ResearchProject, Member, TextContent
from django.utils.html import format_html

@admin.register(ResearchProject)
class ResearchProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date')
    list_editable = ('status','date')
    
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'designation', 'department', 'university')
    search_fields = ('name', 'category', 'university')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploaded_at', 'thumbnail')  # Columns in the admin panel
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
    
    
    