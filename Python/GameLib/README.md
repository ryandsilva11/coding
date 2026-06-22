# Sistema de Biblioteca

## Objetivo

Crie um programa que simule uma biblioteca simples.

O sistema deve permitir que o usuário cadastre, liste, busque e remova livros. Também deve ser possível salvar os dados em um arquivo e carregá-los novamente quando o programa for executado.

## Menu

O programa deve possuir as seguintes opções:

```
1 - Cadastrar livro
2 - Listar livros
3 - Buscar livro
4 - Remover livro
5 - Salvar dados
6 - Carregar dados
0 - Sair
```

## Estrutura de um livro

Cada livro deve possuir as seguintes informações:

* Título
* Autor
* Ano
* Disponibilidade (sim/não)

Exemplo:

```json
{
    "titulo": "O Hobbit",
    "autor": "Tolkien",
    "ano": 1937,
    "disponivel": true
}
```

# Requisitos

## 1. Uso de funções

O programa deve ser organizado utilizando funções.

Não coloque toda a lógica dentro do `while` principal.

Exemplo:

```python
def cadastrar_livro():
    pass

def listar_livros():
    pass
```

---

## 2. Uso de módulos

Organize o projeto da seguinte forma:

```
biblioteca/
│
├── main.py
├── livros.py
└── dados.json
```

### livros.py

Responsável pelas funções relacionadas aos livros:

* Cadastrar livro
* Listar livros
* Buscar livro
* Remover livro

### main.py

Responsável por:

* Controlar o menu
* Receber entradas do usuário
* Gerenciar o fluxo do programa

---

## 3. Arquivo JSON

Os dados dos livros devem ser salvos utilizando um arquivo JSON.

Importe o módulo:

```python
import json
```

Para salvar os dados:

```python
json.dump(lista, arquivo)
```

Para carregar:

```python
json.load(arquivo)
```

O objetivo é que os livros continuem salvos mesmo depois de fechar e abrir o programa novamente.

---

## 4. Tratamento de erros

Utilize `try` e `except` para evitar que o programa quebre.

Exemplos de erros que devem ser tratados:

Usuário informar um ano inválido:

```
ano = "mil novecentos"
```

Tentar carregar um arquivo que ainda não existe.

---

## 5. Sistema de busca

O programa deve permitir buscar livros pelo título.

Exemplo:

Entrada:

```
Buscar: hobbit
```

Resultado:

```
Livro encontrado:
O Hobbit - Tolkien
```

A busca também deve funcionar com letras maiúsculas:

```
HOBBIT
```

Utilize:

```python
.lower()
```

para ignorar diferenças entre maiúsculas e minúsculas.

---

# Conceitos praticados

* Funções
* Módulos
* Listas
* Dicionários
* Manipulação de arquivos
* JSON
* Tratamento de exceções
* Organização de código
