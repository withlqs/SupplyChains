from django.db import models

# Create your models here.

class Attr(models.Model):
    Attri = models.CharField(null = False, max_length = 30)
    Period = models.IntegerField()
    Value = models.DecimalField(max_digits=5, decimal_places=2, null = False)
    class Meta:
        unique_together = ["Attri", "Period", "Value"]

