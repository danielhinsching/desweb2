from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ProdutoPagination(PageNumberPagination):
    """Reproduz o mesmo contrato de paginacao usado em Express/FastAPI (Aula 12):
    { "page": ..., "page_size": ..., "total_pages": ..., "results": [...] }
    em vez do formato padrao do DRF (count/next/previous/results).
    """

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(
            {
                "page": self.page.number,
                "page_size": self.get_page_size(self.request),
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )
