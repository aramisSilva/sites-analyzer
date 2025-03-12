from rest_framework import serializers
from .models import Analise, Site

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'nome', 'url', 'created_at', 'updated_at']


class AnaliseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analise
        fields = ['id', 'site', 'tempo_carregamento', 'seo_score', 'created_at', 'updated_at']