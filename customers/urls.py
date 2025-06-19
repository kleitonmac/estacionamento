from django.urls import path, include
from rest_framework.routers import DefaultRouter

from customers.views import CustomerViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet)  # registrando a rota para o ViewSet

urlpatterns = [
    path('', include(router.urls)),
]

