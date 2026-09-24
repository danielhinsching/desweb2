from django.db import models


class Produto(models.Model):
    """Produto da loja.

    Evoluido na Aula 26 com marca, estoque e descricao, espelhando as Aulas 14-16
    do material de Express/FastAPI. Os campos tem 'default' apenas para permitir
    a migration sobre dados existentes; a obrigatoriedade real de marca/estoque
    e' garantida no ProdutoSerializer (validate_*), nao no Model.
    """

    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=50, default="")
    estoque = models.PositiveIntegerField(default=0)
    descricao = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.nome
