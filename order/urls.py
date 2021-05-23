
from django.contrib import admin
from django.urls import path
from process.views import *
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/',Contact,name='contact'),
    path('review/',review,name='review'),
    path('new/',New,name='new'),
    path('',Index,name='home'),
    path('admin_login/',Login,name='login'),
    path('logout/',Logout_admin,name='logout'),
    path('biography/',Biography,name='biography'),
    path('fiction/',Fiction,name='fiction'),
    path('thriller/',Thriller,name='thriller'),
    path('romance/',Romance,name='romance'),
    path('order/',order,name='order'),
    path('dashboard',dashboard,name='dashboard'),
]



if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
