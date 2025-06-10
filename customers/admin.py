from django.contrib import admin
from customers.models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'phone', 'create_at']  # Campos exibidos na listagem
    search_fields = ['name', 'cpf', 'phone']               # Campos que podem ser pesquisados
