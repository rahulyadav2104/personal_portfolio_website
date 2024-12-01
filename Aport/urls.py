
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('about/',views.about,name='about'),
    path('project/',views.project,name='project'),
    path('certificates/',views.certificates,name='certificates'),
    path('experiences/',views.experiences,name='experiences'),
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)