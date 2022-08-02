from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pizza.routes import router

urlpatterns = [
                  path('', include('pages.urls')),
                  path('pizza/', include('pizza.urls')),
                  path('users/', include('accounts.urls')),
                  path('routes/', include(router.urls)),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = "tizza.views.page_not_found"
