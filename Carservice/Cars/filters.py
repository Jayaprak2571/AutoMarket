import django_filters
from .models import Car

class ProductFilter(django_filters.FilterSet):
    # Custom filters
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    name_contains = django_filters.CharFilter(field_name="make", lookup_expr='icontains')

    class Meta:
        model = Car
        #fields = ['category', 'min_price', 'max_price', 'name_contains']
        fields ='__all__'