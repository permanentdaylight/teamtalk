from django.conf.urls import include, url
from django.contrib import admin
from talk_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('talk_app.urls')),
]
