from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('colaboradores/', include('colaboradores.urls')),
    path('epis/', include('epis.urls')),
    path('entrega/', include('entrega_epi.urls')),
    path('autenticacao/', include('autenticacao.urls')),
    path('perfil/', include('perfil.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]