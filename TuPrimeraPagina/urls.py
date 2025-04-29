"""
URL configuration for TuPrimeraPagina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include  # ✅ necesario para incluir otras rutas
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # ✅ conecta todas las URLs de tu app blog
    path('accounts/', include('accounts.urls')),  # 👈 habilita login/signup/etc.
    path('about/', views.about_view, name='about'),  # 👈 si tenés una vista "about"
    path('pages/', include('pages.urls')),
    path('mensajes/', include('messenger.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
