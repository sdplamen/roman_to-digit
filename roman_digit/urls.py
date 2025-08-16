from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from roman_digit import views

schema_view = get_schema_view(
    openapi.Info(
        title="Roman Numeral Converter API",
        default_version='v1',
        description="API for converting between Roman numerals and integers.",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/to-roman/', views.ToRomanView.as_view(), name='to_roman_api'),
    path('api/to-decimal/', views.ToDecimalView.as_view(), name='to_decimal_api'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]