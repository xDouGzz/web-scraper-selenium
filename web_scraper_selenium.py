"""
web_scraper_selenium.py
=======================
Web scraper utilizando Selenium para extração estruturada de conteúdo HTML.

Funcionalidade:
    - Acessa uma página web com Firefox via Selenium WebDriver
    - Extrai o título principal (H1) e parágrafos da página
    - Organiza os dados em estrutura de dicionário e exibe formatado

Autor: Douglas Melo
Data: Maio/2026
Versão: 1.0.0
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from pprint import pprint
from time import sleep


# ──────────────────────────────────────────────
# Configurações
# ──────────────────────────────────────────────

URL = "https://curso-python-selenium.netlify.app/exercicio_01.html"
WAIT_TIME: int = 3  # Tempo de espera para carregamento da página (segundos)


# ──────────────────────────────────────────────
# Funções
# ──────────────────────────────────────────────

def extrair_titulo(browser: Firefox) -> str:
    """
    Extrai o texto do elemento H1 da página.

    Args:
        browser: Instância ativa do Firefox WebDriver.

    Returns:
        Texto do título principal (H1) como string.
    """
    elemento_h1 = browser.find_element(By.TAG_NAME, "h1")
    return elemento_h1.text


def extrair_paragrafos(browser: Firefox) -> list[str]:
    """
    Extrai o texto de todos os elementos <p> da página.

    Args:
        browser: Instância ativa do Firefox WebDriver.

    Returns:
        Lista de strings com o conteúdo de cada parágrafo.
    """
    elementos_p = browser.find_elements(By.TAG_NAME, "p")
    return [elemento.text for elemento in elementos_p]


def estruturar_dados(titulo: str, paragrafos: list[str]) -> dict:
    """
    Organiza os dados extraídos em um dicionário estruturado.

    Args:
        titulo: Texto do título H1.
        paragrafos: Lista com os textos dos parágrafos.

    Returns:
        Dicionário com título e textos indexados.
    """
    textos_indexados = {
        f"Texto_{i + 1}": texto
        for i, texto in enumerate(paragrafos)
    }

    return {
        "H1": titulo,
        "Textos": textos_indexados,
    }


def executar_scraping(url: str) -> dict | None:
    """
    Orquestra o fluxo completo de scraping: abre o browser,
    acessa a URL, extrai e estrutura os dados, e encerra o browser.

    Args:
        url: Endereço da página a ser acessada.

    Returns:
        Dicionário com os dados extraídos, ou None em caso de erro.
    """
    browser = Firefox()

    try:
        print(f"[INFO] Acessando: {url}")
        browser.get(url)
        sleep(WAIT_TIME)

        titulo = extrair_titulo(browser)
        paragrafos = extrair_paragrafos(browser)
        dados = estruturar_dados(titulo, paragrafos)

        print("[INFO] Extração concluída com sucesso.\n")
        return dados

    except Exception as erro:
        print(f"[ERRO] Falha durante o scraping: {erro}")
        return None

    finally:
        browser.quit()
        print("[INFO] Browser encerrado.")


# ──────────────────────────────────────────────
# Ponto de entrada
# ──────────────────────────────────────────────

if __name__ == "__main__":
    resultado = executar_scraping(URL)

    if resultado:
        print("─" * 40)
        print("Dados extraídos:")
        print("─" * 40)
        pprint(resultado)
