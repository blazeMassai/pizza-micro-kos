from rest_framework import serializers
from pizza.models import Pizza

class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'title', 'description')