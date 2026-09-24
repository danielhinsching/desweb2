import django_filters

from .models import Produto


class ProdutoFilter(django_filters.FilterSet):
    preco_minimo = django_filters.NumberFilter(field_name="preco", lookup_expr="gte")
    preco_maximo = django_filters.NumberFilter(field_name="preco", lookup_expr="lte")
    marca = django_filters.CharFilter(field_name="marca", lookup_expr="iexact")
    estoque_minimo = django_filters.NumberFilter(field_name="estoque", lookup_expr="gte")
    estoque_maximo = django_filters.NumberFilter(field_name="estoque", lookup_expr="lte")

    class Meta:
        model = Produto
        fields = [
            "preco_minimo",
            "preco_maximo",
            "marca",
            "estoque_minimo",
            "estoque_maximo",
        ]
