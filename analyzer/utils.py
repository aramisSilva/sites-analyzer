import requests

def coletar_tempo_carregamento(site_url):
    try:
        response = requests.get(site_url, timeout=10)
        tempo_carregamento = response.elapsed.total_seconds()
        return tempo_carregamento
    except requests.RequestException as e:
        print(f"Erro ao coletar tempo de carregamento do site {site_url}: {e}")
        return None


