from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import (RestaurantSerializer,
                          FoodSerializer)

from ..models import (Restaurant,
                      Food)


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def list(self, request, *args, **kwargs):
        # print('Hi. i\'m a list method!')
        return super(RestaurantViewSet, self).list(request, *args, **kwargs)

    @action(methods=['get'], detail=False)
    def all_instances(self, request, *args, **kwargs):
        queryset = Restaurant.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print(request)
        return super(FoodViewSet, self).dispatch(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print(request.POST)
        return super(FoodViewSet, self).create(request, *args, **kwargs)
