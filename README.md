# BUILTTECH Django Website

Professional Django website for gypsum plastering, false ceiling, partitions and interior finishing.

## 1. Create virtual environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. Install packages
```bash
pip install -r requirements.txt
```

## 3. Create environment file

Copy `.env.example` to `.env` and change the company details.

## 4. Create database
```bash
python manage.py makemigrations
python manage.py migrate
```

## 5. Create admin user
```bash
python manage.py createsuperuser
```

## 6. Start server
```bash
python manage.py runserver
```

Website:
http://127.0.0.1:8000/

Admin:
http://127.0.0.1:8000/admin/

## 7. Add website content

Log in to the admin panel and add:

- Services
- Projects
- Testimonials
- Contact enquiries are automatically saved
- Quote requests are automatically saved

## Logo

The supplied BUILTTECH logo is included at:

`website/static/website/img/logo.png`

Replace it with your final logo if required.

## Production

For deployment, set:
- DEBUG=False
- A strong SECRET_KEY
- Proper ALLOWED_HOSTS
- HTTPS
- PostgreSQL (recommended)
- `python manage.py collectstatic`
