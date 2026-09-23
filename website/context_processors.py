from django.conf import settings

def company_info(request):
    return {
        "company_name": getattr(settings, "COMPANY_NAME", "BUILTTECH ENTERPRICES"),
        "company_phone": getattr(settings, "COMPANY_PHONE", "+91 8921879747"),
        "company_email": getattr(settings, "COMPANY_EMAIL", "builttechenterprises.com@gmail.com"),
        "company_whatsapp": getattr(settings, "COMPANY_WHATSAPP", "+91 8921879747"),
        "company_address": getattr(settings, "COMPANY_ADDRESS", "Kerala, India"),
    }
