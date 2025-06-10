from django.db import models
from customers.models import Customer

class VehicleType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nome')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Tipo de Veículo'
        verbose_name_plural = 'Tipos de Veículos'

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Tipo de Veículo',
    )
    license_plate = models.CharField(max_length=10, unique=True, verbose_name='Placa')
    brand = models.CharField(max_length=50, unique=True, verbose_name='Marca', blank=True, null=True)
    model = models.CharField(max_length=50, verbose_name='Modelo', null=True, blank=True)
    color = models.CharField(max_length=50, verbose_name='Cor', null=True, blank=True)
    owner = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='vehicles',
        verbose_name='Proprietário',
    )
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return f"{self.vehicle_type} - {self.license_plate}"
