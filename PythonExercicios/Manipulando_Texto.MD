from builtins import int

# Manipulando Texto

Um frase é reconhecido pela linguagem de programação como **Cadeia de caracteres** ou simplesmente
como *string*.

Para o Python toda cadeia de texto está em aspas simples *' '* ou aspas duplas *" "*.

## Análise
### Modos de manipular caracteres

 Atribuindo string dentro de uma varíavel.
Exemplo:


###  String
```python
frase = 'Eu sou lindo.'
```


### List
Para criar uma lista:

```python
frase []
```

A função len, de lenght siginifica comprimento.
Então se quisermos saber  quantos caracteres a frase tem, usamos assim:


### Len()
```python
frase = 'Eu sou lindo.'

len(frase)
```

O resultado é que a frase tem 13 caracteres, incluindo os espaços e o ponto final

### Count()
Caso eu queira contar algo em especifco, por exemplo quantas letras *Ós*, temos na frase, realizamos
operação da seguinte forma:

```python
frase = 'Eu sou lindo.'

frase.count('o')
```

Como o exemplo mostra acima, usamos da função count, e passamos a string *o* para contarmos apenas essa letra.


### Find()

Para encontrar algo dentro da sua váriavel string.
No caso vai me dizer onde encontrar o caractere.

No caso abaixo, parte da string *'sou'* está a partir da posição 4

```python
frase = 'Eu sou lindo.'

frase.find('sou')
```

### In

O operador é booleano, e posso validar se existe a palavra tal?
A resposta é *True* ou *False* (Verdadeiro ou Falso)

No caso, a resposta é *True*
```python
frase = 'Eu sou lindo.'

'lindo' in frase
```

## Transformação

Transformação via de regra, uma lista de string ela é imutável, ou seja, não podemos mexer nela.
Mas consigo mudar ela, através de métodos, não conseguindo alterar diretamente os elementos.

### Replace
No exemplo a seguir, a função *replace* vai procurar pela palavra *Eu*, e substituir pela palavra *Nós*.
Também vamos trocar a palavra *sou* pela palavra *somos*

```python
frase = 'Eu sou lindo.'

frase.replace('Eu','Nós')
frase.replace('sou','somos')
```

### Upper
A funcionalidade de upper, serve para alterar as letras que não estão em maiúsculas.
No exemplo abaixo, vamos alterar todas as letras em minúsclulas para maiúsculas

```python
frase = 'Eu sou lindo.'

frase.upper()
```

### Lower
A funcionalidade de lower, serve para alterar as letras que não estão minúsclulas.
No exemplo abaixo, vamos alterar todas as letras em maiúsculas para minúsclulas.

```python
frase = 'Eu sou lindo.'

frase.lower()
```

### Capitalize
O capitalize transformar todos os caracteres para minusculos e apenas o primeiro caractere
da frase ficará em maiúsculo.

Nesse caso ele faz isso na string inteira.


```python
frase = 'Eu sou lindo.'

frase.capitalize()()
```

### Title
De forma semelhante o capitalize, temos a função title, ele trabalha um pouquinho diferente
fazendo uma análise mais profunda.

Ele análisa quantas palavras tem dentro da string, e aí ele faz um capitalize, palavra por palavra.

```python
frase = 'Eu sou lindo.'

frase.title()()
```

### Title
De forma semelhante o capitalize, temos a função title, ele trabalha um pouquinho diferente
fazendo uma análise mais profunda.

Ele análisa quantas palavras tem dentro da string, e aí ele faz um capitalize, palavra por palavra.

```python
frase = 'Eu sou lindo.'

frase.title()()
```

### Strip
Serve pra remover espaços excedentes.

Ele vai remover todos os espaços inúteis, no ínicio e no fim da string.

Também temos as funções *rstrip()* e o *lstrip()*, onde o *rstrip()* remove todos os espaços da direita
e o *lstrip()* remove todos os espaços da esquerda.

```python
frase = '  Eu sou lindo.   '

frase.strip()
frase.rstrip()
frase.lstrip()
```

## Divisão
São funcionalidade criadas para dividir strings.

### Split

Por padrão é feito onde tem espaços, havendo uma divisão da string onde contém espaços.

Tecnicamente, gera uma nova lista com as plavras que foram dividas. Dividindo uma string em uma lista.


```python
frase = '  Eu sou lindo.   '

frase.split()
```

## Junção
São funcionalidade criadas para juntar strings.

### Join

Basicamente, serve para juntar uyma coisa na outra.ecnicamente, gera uma nova lista com as plavras que foram dividas. Dividindo uma string em uma lista.


```python
frase = '  Eu sou lindo.   '

frase.split()
'-'.join(frase)
```