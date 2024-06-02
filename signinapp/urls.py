from django.contrib import admin
from django.urls import path
from signinapp.views import signaction, logaction, storeaction, get_articles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signinapp/signup/', signaction, name='signaction'),
    path('signinapp/login/', logaction, name='logaction'),
    path('signinapp/store/', storeaction, name='storeaction'),
    path('signinapp/get_articles/', get_articles, name='get_articles'),
]

