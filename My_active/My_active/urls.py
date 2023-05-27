"""
URL configuration for My_active project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from active.views import registration


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/registration/', registration, name='registration'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('active/', include('active.urls')),

]


from django.views.generic import RedirectView


urlpatterns += [
    path('', RedirectView.as_view(url='/active/', permanent=True)),
]


from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

