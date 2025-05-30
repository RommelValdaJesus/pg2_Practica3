"""
URL configuration for mi_api project.

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django imports
from django.contrib import admin
from django.urls import path, include

# Django Framework imports
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
# Local imports
from repuestos.views import ProveedorViewSet, MarcaViewSet, VehiculoViewSet, RepuestoViewSet

# Create a router and register our viewsets with it

router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'repuestos', RepuestoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='API Documentation')),
]