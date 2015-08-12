from django.db import models

# Create your models here.

class Attr(models.Model):
    Attri = models.CharField(null=False, max_length=30)
    Period = models.IntegerField()
    Value = models.DecimalField(max_digits=15, decimal_places=4, null=False)

    class Meta:
        unique_together = ["Attri", "Period"]


class Para(models.Model):
    Username = models.CharField(null=False, max_length=30)
    Param = models.CharField(null=False, max_length=30)
    Period = models.IntegerField()
    Value = models.DecimalField(max_digits=15, decimal_places=4, null=False)

    class Meta:
        unique_together = ["Username", "Param", "Period"]
