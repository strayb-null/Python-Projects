import requests
from pywebio.output import put_text, put_buttons, clear
from pywebio import start_server


def get_fato() -> str:
    try:
        resposta = requests.get("https://uselessfacts.jsph.pl/random.json?language=en", timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()
        fun_fact = dados['text']

        return fun_fact
    
    except requests.exceptions.HTTPError:
        status = resposta.status_code

        if status == 404:
            return "Erro 404 -> página não encontrada"

        elif status == 500:
            return "Erro 500 -> servidor da API quebrou"
        
        elif status == 429:
            return "Erro 429 -> Too Many Requests"

        else:
            return f"Erro HTTP: {status}"
        
    except requests.exceptions.ConnectionError:
        return "Erro de conexão -> API fora do ar"
    except requests.exceptions.Timeout:
        return "A API demorou demais para responder"


def app(_=None):
    
    clear()
    put_text("🔄 Buscando curiosidade...")
    texto = get_fato()
    clear()

    put_text(texto)
    put_buttons(["Nova curiosidade"], onclick=app)
    


if __name__ == '__main__':
    start_server(app, port=8080)