from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Service(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    icon = models.CharField(max_length=50, default="fa-layer-group", help_text="Font Awesome icon class")
    featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=120, default="Gypsum Work")
    location = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)
    featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    customer_name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, blank=True)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return self.customer_name


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=180, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.created_at:%Y-%m-%d}"


class QuoteRequest(models.Model):
    PROJECT_TYPES = [
        ("residential", "Residential"),
        ("commercial", "Commercial"),
        ("office", "Office"),
        ("renovation", "Renovation"),
        ("other", "Other"),
    ]
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.CharField(max_length=150)
    project_type = models.CharField(max_length=30, choices=PROJECT_TYPES, default="residential")
    area = models.CharField(max_length=80, blank=True, help_text="Example: 1200 sq.ft")
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_contacted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.location}"
