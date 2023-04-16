## O que é variavel?

É um pequeno espaço na memória do computador para guardar o resultado do usuário que vai digitar.

## Tipos Primitivos

### Inteiro
int ⮕ O tipo inteiro é um tipo composto por caracteres numéricos (algarismos) inteiros.

### Ponto Flutuate ou Decimal
float ⮕ É um tipo composto por caracteres númericos (algarismo) decimais.
informalmente conhecimento como "números quebrados."

### Complexo
complex ⮕ Um tipo de dado usado para representar números complexos (algo parecido com o que estudamos no 3º do ensino médio)
Utilizado normalmente em cálculos geométricos e científicos.

### String
str ⮕ É um conjunto de caracteres dispostos numa determinada ordem, geralmente utilizada pra representar palavras, frases ou textos.

Usar sempre aspas simples *''*  para representar

### Boolean ou Boleano
bool ⮕ Tipo de dado lógico que pode ter apenas um dos dois valores: verdadeiro ou falso (*True* ou *False* no Python)

PS: Quando for usar variavel desse tipo, utilizar a primeira letra maíuscula. *True*

### Listas
list ⮕ Um tipo de dado muito utilizado no dia-a-dia.
Listas agrupam um conjunto de elementos variados. Podendo conter valores, inteiros, floats, strings, outras listas e outros tipos.

Abaixo um exemplo:

``` python
listadecompras = ['arroz', 'farinha', 'macarrão', 'molho de tomate', 'carne']

print(type(listadecompras))
```

## Convertendo um número
 ``` python
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

num1 = int(num1)
num2 = int(num1)
 ```
No trecho de código acima, as variaveis *num1* e *num2* por mais que o usuário digite um número, na verdade é uma
variavel do tipo string.

No segundo bloco do código onde eu digito *num1 = int(num1)* eu estou realizando a conversão do valor da varíavel para 
o tipo int, ou seja, valor inteiro.


## Referencias

[Tipos de Variaveis Disponiveis no Python](https://pythonacademy.com.br/blog/tipos-de-variaveis-no-python) 