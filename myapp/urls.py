from . import views
from .import models
from django.conf.urls import url
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static

app_name="myapp"

urlpatterns=[

    url('home/$',views.home,name='home'),

]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
