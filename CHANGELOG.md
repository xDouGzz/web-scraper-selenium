# 📋 Changelog

Todas as mudanças relevantes deste projeto serão documentadas aqui.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

---

## [1.0.0] — 2026-05-25

### 🚀 Lançamento inicial

- Implementação do scraper para extração de título H1 e parágrafos da página
- Organização dos dados extraídos em dicionário estruturado
- Exibição formatada do resultado com `pprint`
- Encerramento seguro do browser com `browser.quit()`

### 🛠️ Refatoração e boas práticas

- Separação do código em funções com responsabilidade única:
  - `extrair_titulo()` — extrai o H1 da página
  - `extrair_paragrafos()` — extrai todos os parágrafos
  - `estruturar_dados()` — organiza os dados em dicionário
  - `executar_scraping()` — orquestra o fluxo completo
- Adição de **type hints** em parâmetros e retornos
- Adição de **docstrings** no padrão Google Style
- Tratamento de erros com `try / except / finally`
- Definição de constantes `URL` e `WAIT_TIME`
- Proteção do ponto de entrada com `if __name__ == "__main__"`

### 📁 Documentação

- Criação do `README.md` com instruções de instalação e uso
- Criação do `APRENDIZADOS.md` com conceitos e reflexões
- Criação do `CHANGELOG.md`

---

## 🔮 Próximas melhorias planejadas

- [ ] Substituir `sleep()` por `WebDriverWait` (Explicit Waits)
- [ ] Exportar os dados extraídos para um arquivo `.json`
- [ ] Adicionar suporte a múltiplas URLs via linha de comando
