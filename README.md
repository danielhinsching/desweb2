# django-bsi4 — API de Produtos com Django + DRF

Exercício da disciplina de Desenvolvimento Web II (BSI — IFC Araquari), Parte 7 do
[desweb2](https://github.com/marrcandre/desweb2): reimplementar, com Django + Django REST
Framework, o mesmo contrato HTTP já construído em Express e FastAPI nas Partes 1–6.

Sequência seguida (Aulas 17–26): uv → Django → Model → SQLite + Migrations → Django Admin →
DRF → ModelSerializer → ModelViewSet → Router → Swagger/OpenAPI → Validações → Filtros/Busca →
Evolução do Produto.

## Como rodar

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata produtos/fixtures/produtos.json
python manage.py runserver
```

- API: http://localhost:8000/api/produtos/
- Admin: http://localhost:8000/admin/
- Swagger: http://localhost:8000/api/docs/
