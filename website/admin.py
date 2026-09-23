from django.contrib import admin
from .models import ContactMessage, Project, QuoteRequest, Service, Testimonial

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "order")
    list_editable = ("featured", "order")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "short_description")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "location", "completed_date", "featured")
    list_filter = ("category", "featured")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "location", "description")

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "location", "rating")
    list_filter = ("rating",)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "subject", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "phone", "email", "message")
    readonly_fields = ("created_at",)

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "location", "service", "project_type", "created_at", "is_contacted")
    list_filter = ("project_type", "is_contacted", "created_at")
    search_fields = ("name", "phone", "email", "location")
    readonly_fields = ("created_at",)
