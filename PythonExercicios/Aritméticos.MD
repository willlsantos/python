# Operadores Aritméticos

No Python temos alguns operadores aritméticos que são usados na construção de expressões, onde contém um número variado de operandos.

Por exemplo, na expressão `a+b`, temos o operador aritmético `+` e operandos, são as variáveis `a`e `b`.

| Operador                        | Conceito                                                                     | Exemplo |
|---------------------------------|------------------------------------------------------------------------------|---------|      
| + (Adição ou sinal positivo)    | Realiza a soma entre operandos - Adiciona o sinal de positivo ao número      | 10 + 7  |
| - (Subtração ou sinal negativo) | Realiza a subtração entre operandos - Adiciona o sinal de negativo ao número | 10 - 7  |
| * (Multiplicação)               | Realiza a multiplicação entre operandos                                      | 3 * 4   |
| / (Divisão)                     | 	Realiza a divisão entre operandos                                           | 10 / 5  |
| // (Divisão inteira)            | Realiza a divisão entre operandos e a parte decimal do resultado             | 10 // 6 |
| % (Módulo)                      | Retorna o resto da divisão entre operandos                                   | 4 % 2   |
| ** (Exponenciação ou Potência)  | Retorna um número elevado a potência de outro                                | 4 ** 2  |

PS: o símbolo de porcentagem, temos o cálculo do módulo, que é o resto da divisão

O Código abaixo, contém um exemplo usando os operadores mencionados:

```python
numero_1 = 5
numero_2 = 2

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
modulo = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2

print(soma) # 7
print(subtracao) # 3
print(multiplicacao)  # 10
print(divisao) # 2.5
print(divisao_inteira) # 2
print(modulo)  # 1
print(exponenciacao) # 25
```

## Ordem de Precedência

A primeira coisa a ser calculada é o que está dentro do `()` Parentêses.

A segunda coisa a ser calculada são as potências, que são as exponenciações

A Terceira coisa a ser calculada são `*, /, // e %` que são a Multiplicação, Divisão, Divisão inteira e o Módulo (que é o resto da Divisão).
Caso numa expressão tenha alguns desses citados, o cálculo é realizado por quem aparecer primeiro dentro da expressão.

A Quarta coisa a ser calculada é a `+ e -` que são a Soma e a Subtração.

# Referencia

[Operadores no Python](https://www.devmedia.com.br/operadores-no-python/40693)