from django.db import models
from base.custom_models import TimestampMixin

class Site(TimestampMixin):
    url = models.URLField(max_length=200, unique=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Analise(TimestampMixin):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    tempo_carregamento = models.FloatField(null=True, blank=True)
    seo_score = models.FloatField(null=True, blank=True)
