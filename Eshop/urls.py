from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings

admin.site.site_header = 'DSH Store Admin'                    # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'DSH Store from adminsitration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
