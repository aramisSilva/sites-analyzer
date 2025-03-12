from rest_framework import generics, status
from rest_framework.response import Response

from .models import Analise, Site
from .serializers import AnaliseSerializer, SiteSerializer
from rest_framework.views import APIView

from .utils import coletar_tempo_carregamento


class SiteListCreateView(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class SiteDetailView(generics.RetrieveAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class AnaliseListCreateView(generics.ListCreateAPIView):
    queryset = Analise.objects.all()
    serializer_class = AnaliseSerializer

class AnaliseDetailView(generics.RetrieveAPIView):
    queryset = Analise.objects.all()
    serializer_class = AnaliseSerializer

class ColetarAnaliseView(APIView):
    def post(self, request):
        site_url = request.data.get('site_url')
        if not site_url:
            return Response({'error': 'site_url é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
        tempo_carregamento = coletar_tempo_carregamento(site_url)
        if tempo_carregamento is None:
            return Response({'error': 'URL é obrigatória'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        site, _ = Site.objects.get_or_create(url=site_url, nome=site_url.split('/')[2])
        analise = Analise.objects.create(site=site, tempo_carregamento=tempo_carregamento)

        return Response({'mensage': 'Análise realizada com sucesso', 'tempo_carregamento': tempo_carregamento} )