from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from load_data.models import Stock



class StockResource(ModelResource):
    class Meta:
        queryset = Stock.objects.all().filter(instock=0)
        resource_name = 'stock'
        allowed_methods = ['get']
        fields = ['instock', 'cod_local', 'cod_mat', 'description']
        excludes = ['resource_uri']
        filtering = {
            'cod_local': ALL,
            'cod_mat': ALL
        }

