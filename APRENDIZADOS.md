# 📖 Aprendizados

Registro do que foi aprendido e praticado durante o desenvolvimento deste projeto.

---

## 🎯 Objetivo do Projeto

Solucionar o **Exercício 01** do curso *Selenium com Python* do canal [Eduardo Mendes (Dunossauro)](https://www.youtube.com/@Dunossauro), que consiste em acessar uma página web automaticamente, extrair seu conteúdo e organizá-lo em uma estrutura de dados.

---

## 🧠 Conceitos Praticados

### Selenium WebDriver
- Inicializar um browser (Firefox) de forma automatizada via código
- Navegar para uma URL com `browser.get()`
- Localizar elementos HTML pelo tipo de tag com `By.TAG_NAME`
- Diferenciar `find_element` (um elemento) de `find_elements` (lista de elementos)
- Encerrar o browser corretamente com `browser.quit()`

### Python
- Organizar dados extraídos em **dicionários** estruturados
- Utilizar **list comprehension** para simplificar a criação de listas
- Aplicar **type hints** para documentar tipos de parâmetros e retornos
- Escrever **docstrings** para descrever o comportamento das funções
- Usar `pprint` para exibir dicionários de forma legível no terminal
- Separar responsabilidades com funções bem definidas

### Boas Práticas
- Utilizar `try / except / finally` para garantir que o browser seja encerrado mesmo em caso de erro
- Definir constantes no topo do arquivo (`URL`, `WAIT_TIME`)
- Proteger o ponto de entrada com `if __name__ == "__main__"`

---

## 🚧 Dificuldades Encontradas

- Entender a diferença entre `find_element` e `find_elements` e quando usar cada um
- Compreender a necessidade do `sleep()` para aguardar o carregamento da página antes de interagir com os elementos

---

## 🔄 O que eu faria diferente hoje

- Substituir o `sleep()` fixo por **Explicit Waits** do Selenium (`WebDriverWait`), que aguardam o elemento estar disponível de forma mais inteligente e eficiente
- Salvar os dados extraídos em um arquivo `.json` ao invés de apenas exibir no terminal

---

## 📚 Referências

- [Curso Selenium com Python — Eduardo Mendes](https://www.youtube.com/watch?v=Pax0jiAcTWs&list=PLOQgLBuj2-3LqnMYKZZgzeC7CKCPF375B&index=21)
- [Documentação oficial do Selenium](https://www.selenium.dev/documentation/)
- [Documentação Python — Type Hints](https://docs.python.org/3/library/typing.html)
