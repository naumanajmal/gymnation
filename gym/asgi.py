"""
ASGI config for gym project.

It exposes the ASGI callable as a module-level variable named ``app``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from fastapi import FastAPI
from gymapp.api.main import app as fastapi_app  # Import your FastAPI app here
from django.core.asgi import get_asgi_application
from fastapi.middleware.wsgi import WSGIMiddleware

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym.settings')

# Create Django ASGI application
django_app = get_asgi_application()

# Create FastAPI application
app = FastAPI()

# Mount applications
app.mount("/api", WSGIMiddleware(django_app))  # Mount Django under "/api"
app.mount("/fastapi", fastapi_app)            # Mount FastAPI under "/fastapi"
