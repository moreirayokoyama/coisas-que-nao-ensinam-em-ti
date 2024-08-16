---
title: 2.4 - Composição de Comandos e Operações Lógicas
---

Bash suporta uma forma de criar uma composição de comandos em uma única instrução usando o separador `;`. Por exemplo:

```bash
echo "Olá mundo"; date ; echo "Bom trabalho."
```

Outra forma de compor comandos em uma única instrução é usando o operador `&`. A diferença entre compor comandos com `;` e `&`, é que com `;` ele sempre executa o comando seguido por `;` de forma síncrona, esperando o fim da sua execução antes de executar o próximo, enquanto que com `&`, o bash executa cada comando seguido por `&` em um novo processo assíncrono, e inicia a execução do próximo sem aguardar a sua finalização.

Instruções como esta acima executam cada comando na ordem em que eles são escritos, mas sem conectá-los de forma alguma (como vimos na aula anterior na seção [Conectando Programas](../01-shell/07-conectando-programas.md)).

Usar este tipo de composição executa todos os comandos independente do resultado de qualquer um deles. Se houver um erro em algum comando desta cadeia, isso não fará com que o bash deixe de executar os demais comandos.

Existem cenários onde a execução de alguns comandos da composição pode gerar resultados que afetem o funcionamento dos demais comandos. Para estes cenários, usamos operações lógicas.

Bash, como qualquer outra linguagem de programação suporta certos tipos de operações lógicas. Operações lógicas são operações que geram resultados binários (_verdadeiro_ ou _falso_), e que podem ser usadas para criar uma composição de comandos baseada no resultado dos comandos usados.

Os operadores lógicos que usaremos aqui são o `||` (operador _OU_) e o `&&` (operador _E_). E os valores lógicos em Bash são `true` (representa o valor _verdadeiro_) e `false` (que representa o valor _falso_).

Vamos ver alguns exemplos básicos de expressões lógicas:
```bash
echo true
echo false

echo true || true
echo true || false
echo false || true
echo false || false

echo true && true
echo true && false
echo false && true
echo false && false
```

Os operadores lógicos possuem a capacidade de garantir certos resultados baseados no valor dos operandos: O operador `||` (_OU_) resulta em `true` (_verdadeiro_) quando qualquer um dos operandos, ou ambos, são verdadeiros, e só resulta em `false`(_falso_) quando ambos os operandos são falsos. Por outro lado, o operador `&&` (_E_), só resulta em true quando ambos os operandos são verdadeiros, mas resulta em false quando qualquer um deles, ou ambos, são false.

Ambos os operadores também possuem a propriedade de descartar o segundo operando de acordo com certos critérios sobre o primeiro. Por exemplo, por que o operador `||` resulta em `true` caso qualquer operando seja verdadeiro, se o primeiro operando (à esquerda do operador) resultar em `true`, o operador descarta qualquer que seja o valor do segundo operando (à direita do operador) e resulta imediatamente em `true`.

Já o operador `&&`, que resulta `false` caso qualquer um dos operandos seja falso, descarta o segundo operando quando o primeiro já resultou em `false`, antecipando o resultado da operação.

Estas propriedades são úteis, principalmente quando consideramos que um comando executado sem resultar em erros é considerado como resultando em `true`, mas caso resulte em qualquer erro tem sua execução resultando como valor `false`. Por exemplo:

```bash
true || echo "Este comando NÃO SERÁ executado"
false || echo "Este comando SERÁ executado"
true && echo "Este comando SERÁ executado"
false && echo "Este comando NÃO SERÁ executado"
```

Isto torna possível criarmos uma composição mais sofisticada de comandos, fazendo com que o resultado de alguns comandos influenciem a execução ou não dos demais.

```bash
echo "Olá mundo" || echo "Este comando NÃO SERÁ executado"
mv xpto.txt ~ || echo "Houve algum problema no comando anterior"
echo "Esta linha será exibida" && echo "Esta também"
mv xpto.txt ~ || (echo "Houve algum problema no comando anterior, criando o arquivo vazio" && touch ~/xpto.txt)
```

Desta forma podemos decidir se queremos apenas que os comandos sejam executados de forma independente (usando o separador `;`), ou se queremos usar o resultado dos comandos intermediários na composição para definirmos se os comandos posteriores serão ou não executados.
