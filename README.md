# 🌐 Web Scraper com Selenium

Scraper para extração estruturada de conteúdo HTML utilizando Python e Selenium WebDriver.

> 💡 Este projeto foi desenvolvido como resposta a um desafio prático do curso **Selenium com Python**, do canal [Eduardo Mendes (Dunossauro)](https://www.youtube.com/@Dunossauro) no YouTube.

---

## 📋 Pré-requisitos

- Python 3.12 ou superior → [python.org/downloads](https://www.python.org/downloads/)
- Firefox instalado na máquina → [mozilla.org/firefox](https://www.mozilla.org/firefox/)
- GeckoDriver compatível com sua versão do Firefox → [github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)

> **GeckoDriver:** baixe o executável, extraia e adicione ao PATH do sistema.

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git git clone https://github.com/xDouGzz/web-scraper-selenium.git
cd web-scraper-selenium
```

### 2. Crie o ambiente virtual (venv)

```bash
# Windows
python -m venv venv

# Linux / macOS
python3 -m venv venv
```

### 3. Ative o ambiente virtual

```bash
# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

> Após ativar, o terminal exibirá `(venv)` no início da linha.

### 4. Instale as dependências

```bash
pip install selenium
```

Ou, se o projeto tiver um `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## ▶️ Execução

Com o ambiente virtual ativo, execute:

```bash
python web_scraper_selenium.py
```

**Saída esperada:**

```
[INFO] Acessando: https://curso-python-selenium.netlify.app/exercicio_01.html
[INFO] Extração concluída com sucesso.

----------------------------------------
Dados extraídos:
----------------------------------------
{'H1': '...',
 'Textos': {'Texto_1': '...',
            'Texto_2': '...',
            'Texto_3': '...'}}
[INFO] Browser encerrado.
```

---

## 📦 Gerando o requirements.txt

Após instalar as dependências, salve-as para facilitar o uso por outras pessoas:

```bash
pip freeze > requirements.txt
```

---

## 🛑 Desativando o ambiente virtual

Quando terminar, desative o venv com:

```bash
deactivate
```

---

## 🗂️ Estrutura do Projeto

```
📁 seu-repositorio/
├── web_scraper_selenium.py   # Script principal
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação
```

---

## 🛠️ Tecnologias

| Tecnologia | Versão |
|---|---|
| Python | 3.12+ |
| Selenium | 4.x |
| Firefox + GeckoDriver | Mais recente |

---

## 📚 Referências

Este script é a solução do **Exercício 01** do curso *Selenium com Python*:

| | |
|---|---|
| **Curso** | Selenium com Python |
| **Instrutor** | Eduardo Mendes (Dunossauro) |
| **Canal** | [youtube.com/@Dunossauro](https://www.youtube.com/@Dunossauro) |
| **Aula** | [Assistir no YouTube](https://www.youtube.com/watch?v=Pax0jiAcTWs&list=PLOQgLBuj2-3LqnMYKZZgzeC7CKCPF375B&index=21) |

---

## 👤 Autor

Feito por **Douglas Melo** — [LinkedIn](https://www.linkedin.com/in/douglas-melo-8a2877214/) · [GitHub](https://github.com/xDouGzz)
