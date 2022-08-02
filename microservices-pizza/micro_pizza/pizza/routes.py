from rest_framework import routers
from pizza.viewsets import PizzaViewSet


router = routers.DefaultRouter()
router.register(r'api/v1/pizzas', PizzaViewSet)