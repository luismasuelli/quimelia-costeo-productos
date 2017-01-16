"""quimelia_gestion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import geo.admin
import contacts.admin
import materials.admin
import contacts.urls
import materials.urls
import main.urls

geo.admin.register(admin.site)
contacts.admin.register(admin.site)
materials.admin.register(admin.site)

urlpatterns = [
    url(r'', include(main.urls)),
    url(r'^contacts/', include(contacts.urls)),
    url(r'^materials/', include(materials.urls)),
    url(r'^admin/', admin.site.urls),
]
