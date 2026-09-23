from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from urllib.parse import quote as urlquote
from .forms import ContactForm, QuoteForm
from .models import Project, Service, Testimonial

def home(request):
    context = {
        "services": Service.objects.filter(featured=True)[:6],
        "projects": Project.objects.filter(featured=True)[:6],
        "testimonials": Testimonial.objects.all()[:6],
    }
    return render(request, "website/home.html", context)

def about(request):
    return render(request, "website/about.html")

def services(request):
    return render(request, "website/services.html", {"services": Service.objects.all()})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, "website/service_detail.html", {"service": service})

def projects(request):
    return render(request, "website/projects.html", {"projects": Project.objects.all()})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "website/project_detail.html", {"project": project})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your message has been sent. We will contact you soon.")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "website/contact.html", {"form": form})

def quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()

            message = "*New Quote Request - Builtech Enterprises*\n\n"

            for field_name, field in form.fields.items():
                value = form.cleaned_data.get(field_name)

                if value:
                    message += f"*{field.label}:* {value}\n"

            whatsapp_number = "918921879747"

            whatsapp_url = (
                f"https://wa.me/{whatsapp_number}"
                f"?text={urlquote(message)}"
            )

            return redirect(whatsapp_url)

    else:
        form = QuoteForm()
    return render(request, "website/quote.html", {"form": form})
