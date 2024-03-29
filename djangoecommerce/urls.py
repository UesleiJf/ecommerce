"""djangoecommerce URL Configuration

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

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

from core import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^entrar/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^sair/$', LogoutView.as_view(template_name='index.html'), name='logout'),
    url(r'^catalogo/', include(('catalog.urls', 'catalog'), namespace='catalog')),
    url(r'^conta/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    url(r'^compras/', include(('checkout.urls', 'checkout'), namespace='checkout')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
