from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .filters import ProdutoFilter
from .models import Produto
from .pagination import ProdutoPagination
from .serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    """CRUD completo de produtos, com filtros, busca, ordenacao e paginacao.

    - Filtros: ?preco_minimo=100&preco_maximo=1000
    - Busca: ?search=mouse (case-insensitive, parcial, no nome)
    - Ordenacao: ?ordering=nome | -nome | preco | -preco
    - Paginacao: ?page=1&page_size=10
    """

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    pagination_class = ProdutoPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = ProdutoFilter
    search_fields = ["nome"]
    ordering_fields = ["nome", "preco"]
