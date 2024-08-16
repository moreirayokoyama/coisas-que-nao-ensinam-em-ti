---
title: 2.5 - Expansões de Chave
---

_Expansões de Chave_ são um tipo específico de expansão do shell, como os que vimos anteriormente (`$()` e `$(())`), que usa expressões cercadas por chaves (`{}`) para expandir para um conjunto de valores. Por exemplo:

 ```bash
 echo a{b,c,d}e
 ```
 A linha acima vai expandir a expressão `a{b,c,d}e` para `abe ace ade`. Note algumas coisas:
 - Cada elemento dentro das chaves foi usado para materializar um elemento no resultado final
 - O resultado foi a expansão dos elementos separados por espaço, na ordem em que eles estão dentro das chaves

É possível combinar mais de uma expansão de chaves na mesma expressão:
```bash
echo ab{c,d}{e,f}gh
```

Não precisamos nos limitar a apenas conjuntos de elementos formados por uma única letra, mas podemos usar valores de tamanhos variados.

```bash
echo ab{cde,fghi}j
```

O exemplo acima mostra uma expansão com apenas dois elementos, cada um com um tamanho diferente.

Também podemos expandir os elementos dentro das chaves para o intervalo de uma sequência ncremental usando a expansão `..`. Por exemplo:
```bash
echo {1..9}
echo {a..z} # podemos usar letras no lugar de números
echo a{1..5}{b..f}g
```

Podemos também controlar a forma como estas sequências são incrementadas:
```bash
echo {1..9..2} # Incrementa de dois em dois
echo {1..9..3} # ou de três em três
echo {a..z..3} # também funciona com letras
```

O fato de expansões deste tipo serem formadas com os elementos separados por espaço as tornam úteis quando usamos estas expansões com comandos que recebem múltiplos argumentos e que podem ser usados de forma mais produtiva. Por exemplo:

```bash
mkdir {foo,bar} # cria dois diretórios
touch {foo,bar}/{a..h}.{txt,sh} # cria nos dois diretórios um conjunto arquivos .txt
mkdir baz
cp foo/{a..h..2}.txt baz
cp bar/{a..h..2}.sh baz
```
