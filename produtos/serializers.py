from decimal import Decimal

from rest_framework import serializers

from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    # Sobrescritos explicitamente para controlar obrigatoriedade e limites,
    # independente do 'default' do Model (que existe so' por causa da migration).
    marca = serializers.CharField()
    estoque = serializers.IntegerField(min_value=0)
    descricao = serializers.CharField(
        required=False, allow_null=True, allow_blank=True, max_length=500
    )

    class Meta:
        model = Produto
        fields = ["id", "nome", "preco", "marca", "estoque", "descricao"]

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

    def validate_marca(self, value):
        marca = value.strip()
        if len(marca) < 2 or len(marca) > 50:
            raise serializers.ValidationError(
                "A marca deve possuir entre 2 e 50 caracteres."
            )
        return marca
