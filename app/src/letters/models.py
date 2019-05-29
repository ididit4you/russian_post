from django.db import models
from project.models import BaseModel

# Create your models here.

class Letter(BaseModel):
    barcode = models.BigIntegerField('Трек-номер', null=True, blank=True)
    def __str__(self):
        return str(self.barcode)