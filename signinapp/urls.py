from django.contrib import admin
from django.urls import path , include
from signinapp.views import signaction,logaction,storeaction
urlpatterns = [
    path('admin/', admin.site.urls),
     path('signinapp/', logaction , name='logaction'),
     path('signinapp/', signaction , name='signaction'),
      path('signinapp/', storeaction , name='storeaction'),
]