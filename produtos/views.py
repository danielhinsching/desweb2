from rest_framework import viewsets

from .models import Produto
from .serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    """CRUD completo de produtos: list, retrieve, create, update, partial_update, destroy."""

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
