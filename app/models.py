from django.db import models
import os
# Create your models here.
class Activo(models.Model):
    id_activo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=1024, blank=True, null=True)
    descripcion = models.CharField(max_length=1024, blank=True, null=True)
    codigo = models.IntegerField()
    ubicacion = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'activo'

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'

class TipoFotografia(models.IntegerChoices):
    ACTIVO = 0, 'A'
    CODIGO = 1, 'B'
    SERIE = 2, 'C'

def renombrar(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.id_activo.codigo}{instance.get_tipo_display()}.{ext}'
    path = f'app/static/photos/{instance.id_activo.ubicacion}/{instance.id_activo.codigo}'
    return os.path.join(path,filename)

class Fotografia(models.Model):
    id_fotografia = models.AutoField(primary_key=True)
    id_activo = models.ForeignKey(Activo, models.DO_NOTHING, )
    fotografia = models.ImageField(upload_to=renombrar, blank=True, null=True)
    tipo = models.IntegerField(default=TipoFotografia.ACTIVO,
                               choices=TipoFotografia.choices)

    class Meta:
        managed = True
        db_table = 'fotografia'

    def __str__(self):
        return f'{self.id_activo.codigo}{self.get_tipo_display()}'

