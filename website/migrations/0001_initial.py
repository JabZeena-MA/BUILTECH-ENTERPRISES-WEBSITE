from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django.db.models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=150)),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("short_description", models.CharField(max_length=250)),
                ("description", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="services/")),
                ("icon", models.CharField(default="fa-layer-group", help_text="Font Awesome icon class", max_length=50)),
                ("featured", models.BooleanField(default=True)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["order", "title"]},
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=180)),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("category", models.CharField(default="Gypsum Work", max_length=120)),
                ("location", models.CharField(blank=True, max_length=150)),
                ("description", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="projects/")),
                ("completed_date", models.DateField(blank=True, null=True)),
                ("featured", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("customer_name", models.CharField(max_length=120)),
                ("location", models.CharField(blank=True, max_length=120)),
                ("message", models.TextField()),
                ("rating", models.PositiveSmallIntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("phone", models.CharField(max_length=30)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("subject", models.CharField(blank=True, max_length=180)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_read", models.BooleanField(default=False)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="QuoteRequest",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("phone", models.CharField(max_length=30)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("location", models.CharField(max_length=150)),
                ("project_type", models.CharField(choices=[("residential","Residential"),("commercial","Commercial"),("office","Office"),("renovation","Renovation"),("other","Other")], default="residential", max_length=30)),
                ("area", models.CharField(blank=True, help_text="Example: 1200 sq.ft", max_length=80)),
                ("message", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_contacted", models.BooleanField(default=False)),
                ("service", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="website.service")),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
