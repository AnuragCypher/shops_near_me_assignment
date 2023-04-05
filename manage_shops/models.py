from django.contrib.gis.db import models as gis_models
from django.db import models
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations

class Migration(migrations.Migration):

    operations = [
        CreateExtension('postgis'),
    ]

class Shops(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    location = gis_models.PointField(u"longitude/latitude",geography=True, blank=True, null=True)

    def __str__(self):
        return self.name
