import django_filters

from .models import Produto


class ProdutoFilter(django_filters.FilterSet):
    preco_minimo = django_filters.NumberFilter(field_name="preco", lookup_expr="gte")
    preco_maximo = django_filters.NumberFilter(field_name="preco", lookup_expr="lte")

    class Meta:
        model = Produto
        fields = ["preco_minimo", "preco_maximo"]
