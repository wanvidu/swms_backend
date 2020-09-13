from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from reservoirs.views import ReservoirViewset
from water_level.views import WaterLevelViewset
from water_level_prediction.views import WaterLevelPredictionViewSet
from water_consumption_prediction.views import WaterConsumptionPredictionViewSet
from home_details.views import HomeViewset, HomeWaterConsumptionViewset

schema_view = get_schema_view(
    openapi.Info(
        title="SWMS API",
        default_version='v1',
        description="API for SWMS",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'reservoirs', ReservoirViewset)
router.register(r'water_level', WaterLevelViewset)
router.register(r'water_level_prediction',
                WaterLevelPredictionViewSet, basename='water_level_prediction')
router.register(r'water_level_consumption',
                WaterConsumptionPredictionViewSet, basename='water_level_consumption')
router.register(r'homes', HomeViewset)
router.register(r'home_details', HomeWaterConsumptionViewset)


urlpatterns = [
    path('', include(router.urls)),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
