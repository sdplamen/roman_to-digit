from django.urls import path
from roman_digit import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('', views.index, name='index'),
    path('api/to-roman/', views.ToRomanView.as_view(), name='to_roman_api'),
    path('api/to-decimal/', views.ToDecimalView.as_view(), name='to_decimal_api'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/',SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]