from decimal import Decimal

from rest_framework import serializers

from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "nome", "preco"]

    def validate_nome(self, value):
        nome = value.strip()
        if len(nome) < 2 or len(nome) > 100:
            raise serializers.ValidationError(
                "O nome deve possuir entre 2 e 100 caracteres."
            )
        return nome

    def validate_preco(self, value):
        if value <= Decimal("0"):
            raise serializers.ValidationError("O preco deve ser maior que zero.")
        return value
