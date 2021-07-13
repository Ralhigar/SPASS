from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Eje)
class EjeAdmin(admin.ModelAdmin):
    list_display = ("id",'nombre',"estrategia","problema",)
    search_fields = list_display
    ordering = ('nombre',)


@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('id',"resultado",
        "presupuesto",
        "eje")
    search_fields = list_display[0:3] + ("eje__nombre",)
    ordering = ('id',)
    

@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display = ('id',
        "codigo",
        "nombre",
        "fuente_verificacion",
        "formula",
        "plazo",
        "resultado",
    )
    search_fields = (
        "codigo",
        "nombre",
        "fuente_verificacion",
        "formula",
        "plazo",
        "resultado__resultado",
    )
    filter_horizontal = (
        "instituciones",
        "variables",
        "fuentes_informacion",
    )
    ordering = ('id',)


@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('id',
        "nombre",
        "codigo",
    )
    search_fields = list_display
    ordering = ('id',)


@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    list_display = ('id',
        "nombre",
        "codigo",
    )
    search_fields = list_display
    ordering = ('id',)


@admin.register(UnidadMedida)
class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = ('id',
        "nombre",
        "codigo",
        "variable"
    )
    search_fields = ('id',
        "nombre",
        "codigo",
        "variable__nombre")
    ordering = ('id',)


@admin.register(FuenteInformacion)
class FuenteInformacionAdmin(admin.ModelAdmin):
    list_display = ('id',
        "nombre",
        "codigo",
    )
    search_fields = list_display
    ordering = ('id',)

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('id',
    "codigo",
    "contenido",
    "indicador",
    "municipio",
    )
    filter_horizontal = (
        "factores",
    )
    search_fields = ('id',"codigo","contenido")
    ordering = ('id',)
    
    
@admin.register(FactorDesagregacion)
class FactorDesagregacionAdmin(admin.ModelAdmin):
    list_display = ('id',
        "nombre",
        "codigo",
    )
    search_fields = list_display
    ordering = ('id',)

    
@admin.register(ValorFactor)
class ValorFactorAdmin(admin.ModelAdmin):
    list_display = ('id',
    "valor",
    "codigo",
    "factor",
    )
    search_fields = ('id',
    "valor",
    "codigo",)
    ordering = ('id',)


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('id',
    "nombre",
    "codigo",
    "Departamento",
    )
    search_fields = ('id',
    "nombre",
    "codigo",
    "Departamento__nombre",)
    ordering = ('id',)

    
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id',
        "nombre",
        "codigo",
    )
    search_fields = list_display
    ordering = ('id',)
