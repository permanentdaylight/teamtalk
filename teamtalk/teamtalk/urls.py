from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from talk_app import views

router = routers.DefaultRouter()
router.register(r'teams', views.TeamsViewSet)
router.register(r'players', views.PlayersViewSet)
router.register(r'coaches', views.CoachesViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('talk_app.urls')),
    url(r'^api/', include(router.urls)),
]
