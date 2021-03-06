"""FantasticFiesta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include

from dashboard.views import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),
    url(r'^$', DashboardView.as_view(), name="dashboard"),
    path('account/', include(('login.urls', 'login'), namespace='login')),
    path('event/', include(('event.urls', 'event'), namespace='event')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
