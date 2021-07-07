from django.db import models

# Create your models here.
class Eje(models.Model):
    nombre = models.CharField(("Nombre"), max_length=50)
    estrategia = models.TextField(("Estrategia"))
    problema = models.TextField(("Problema"))

    class Meta:
        verbose_name = ("Eje")
        verbose_name_plural = ("Ejes")

    def __str__(self):
        return self.nombre


class Resultado(models.Model):
    resultado = models.TextField(("Resultado"))
    presupuesto = models.TextField(("Presupuesto"))
    eje = models.ForeignKey("violencia.Eje", verbose_name=(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Resultado'
        verbose_name_plural = 'Resultados'

    def __str__(self):
        return f'{self.resultado}' 


class Indicador(models.Model):
    codigo = models.CharField(("codigo"), max_length=50)
    nombre = models.CharField(("Nombre"), max_length=150)
    fuente_verificacion = models.TextField(("Fuente de Verificacion"))
    formula = models.TextField(("Formula"))
    plazo = models.IntegerField(("Plazo"), default=1, choices=((1,"Corto"),(2,"Medio"),(3,"Largo")))
    resultado = resultado = models.ForeignKey("violencia.Resultado", on_delete=models.CASCADE)
    instituciones = models.ManyToManyField("violencia.Institucion", related_name="indicadores")
    variables = models.ManyToManyField("violencia.Variable",related_name="indicadores")
    fuentes_informacion = models.ManyToManyField("violencia.FuenteInformacion",related_name="indicadores")

    class Meta:
        verbose_name = 'Indicador'
        verbose_name_plural = 'Indicadores'

    def __str__(self):
        return f'{self.codigo}'


class Institucion(models.Model):
    nombre = models.CharField("Nombre",max_length=100)
    codigo = models.CharField("Codigo",max_length=50)

    class Meta:
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'

    def __str__(self):
        return f'{self.nombre}'


class Variable(models.Model):
    nombre = models.CharField("Nombre",max_length=100)
    codigo = models.CharField("Codigo",max_length=50)

    class Meta:
        verbose_name = 'Variable'
        verbose_name_plural = 'Variables'

    def __str__(self):
        return f'{self.nombre}'


class UnidadMedida(models.Model):
    nombre = models.CharField("Nombre",max_length=100)
    codigo = models.CharField("Codigo",max_length=50)
    variable = models.ForeignKey("violencia.Variable", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        return f'{self.nombre}'


class FuenteInformacion(models.Model):
    nombre = models.CharField("Nombre",max_length=100)
    codigo = models.CharField("Codigo",max_length=50)

    class Meta:
        verbose_name = 'Fuente de Informacion'
        verbose_name_plural = 'Fuentes de Informacion'

    def __str__(self):
        return f'{self.nombre}'


class Reporte(models.Model):
    codigo = models.CharField("Codigo",max_length=50)
    contenido = models.TextField("Contenido")
    indicador = models.ForeignKey('violencia.Indicador',related_name=("reportes"), on_delete=models.CASCADE)
    municipio = models.ForeignKey("violencia.Municipio",related_name=("reportes"), on_delete=models.CASCADE)
    factores = models.ManyToManyField("violencia.FactorDesagregacion",related_name="reportes")
    
    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'

    def __str__(self):
        return f'{self.codigo}'

class FactorDesagregacion(models.Model):
    nombre = models.CharField("Nombre",max_length=50)
    
    class Meta:
        verbose_name = 'FactorDesagregacion'
        verbose_name_plural = 'Factores de Desagregacion'

    def __str__(self):
        return f'{self.nombre}'


class ValorFactor(models.Model):
    valor = models.CharField("Valor",max_length=200)
    codigo = models.CharField("Codigo",max_length=4)

    class Meta:
        verbose_name = 'Valor de Factor'
        verbose_name_plural = 'Valor de Factores'

    def __str__(self):
        return f'{self.valor}'


class Municipio(models.Model):
    nombre = models.CharField("Nombre",max_length=50)
    codigo = models.CharField("Codigo",max_length=10)
    Departamento = models.ForeignKey("violencia.Departamento", on_delete=models.CASCADE, related_name="departamento")
    
    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return f'{self.nombre }' # TODO


class Departamento(models.Model):
    nombre = models.CharField("Nombre",max_length=50)
    codigo = models.CharField("Codigo",max_length=10)
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return f'{self.nombre}' # TODO


