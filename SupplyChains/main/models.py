from django.db import models

# Create your models here.

class Attributes(models.Model):
    ChainID = models.CharField(null = False, max_length = 15)
    Attribute = models.CharField(null = False, max_length = 30)
    Period = models.IntegerField()
    Value = models.DecimalField(null = False)
    class Meta:
        unique_together = {"ChainID", "Attribute", "Period"}
