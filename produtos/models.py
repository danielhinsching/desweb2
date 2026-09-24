from django.db import models


class Produto(models.Model):
    """Representa um produto da loja.

    Começa com os mesmos campos usados nas Aulas 2-13 (Express/FastAPI): nome e preco.
    Os campos marca, estoque e descricao serão adicionados na Aula 26 (Evolução do Produto),
    espelhando as Aulas 14-16 do material de Express/FastAPI.
    """

    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.nome
