---
title: 2.2 - Expressões e Expansões do Shell
---

O uso de delimitadores, como o que usamos para definir o argumento `"Hello world"` para o comando `echo`, é um exemplo de uma _expressão_. Expressões são formas de criar valores em uma linguagem de programação, e em Bash não é diferente. Expressões de textos são as mais simples que podemos usar, mas existem outros tipos de expressões, e falaremos um pouco sobre alguns deles.

Um tipo de expressão comum em Bash, são expressões que expandem seu conteúdo baseado em algumas operações disponíveis. Existem vários tipos de expansões que podemos utilizar quando escrevemos expressões em Bash. Uma delas é, por exemplo, expandir o resultado da execução de um comando para utilizá-lo em uma instrução. Para criar expressões deste tipo, usamos a expansão `$(<comando-bash>)`.

```bash
echo $(ls)
```

A linha acima executa o comando `ls` e usa a saída como uma expressão que é então passada para o comando `echo`. O resultado é semelhante à execução do comando `ls` no shell (a exibição da lista de arquivos). A diferença é que podemos usar esta expansão em outras operações, não apenas para exibí-las (usando o comando `echo`), mas também, por exemplo, atribuir este valor a variáveis e reutilizá-las para outros fins, como veremos em breve.

É possível, também, expandir expressões aritméticas e exibir seu resultado. Para criarmos uma expressão aritmética, usamos a expansão `$(( <expressão-aritmética> ))`. Desta forma, o shell não tentará interpretar a expressão como se fosse um comando.

```bash
echo $((7 + 8))
echo $((7 * 8))
echo $(((7 - 3) / (8 % 3)))
```
