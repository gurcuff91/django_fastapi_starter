"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.apps import apps
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles

# Configure Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
apps.populate(settings.INSTALLED_APPS)

# This endpoint imports should be placed below the settings env declaration
# Otherwise, django will throw a configure() settings error
from project.urls import api_router

# Get the Django WSGI application we are working with
django_app = get_wsgi_application()


def get_asgi_application() -> FastAPI:
    app = FastAPI(title="Django FastApi Starter", debug=settings.DEBUG)
    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Add Api Router
    app.include_router(api_router)
    # Mount Django
    app.mount("/dj", WSGIMiddleware(django_app))
    # Set Up the static files and directory to serve Django static files
    app.mount(settings.STATIC_URL, StaticFiles(directory="static"), name="static")

    return app


application = get_asgi_application()
