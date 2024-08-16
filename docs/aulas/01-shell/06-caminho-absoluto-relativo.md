---
title: 1.6 - Caminho Absoluto, Caminho Relativo e Caracteres Coringa
---
Até aqui, temos usado o que chamamos de _Caminho Absoluto_ (Absolute Path) para endereçar os arquivos e diretórios que usamos. Mas existem atalhos especiais que nos ajudam a facilitar a descrição de caminhos baseados no diretório atual em que nos localizamos.

Uma das opções disponíveis no comando `ls` é a opção `-a` ou `--all`, que deixam de ignorar certos arquivos que normalmente não são exibidos. Por padrão, os arquivos que começam com `.` (ponto), ficam ocultos normalmente no comando `ls`. Vamos ver quais arquivos visualizamos ao usar esta opção:

```bash
ls -lha
```

Dentre os novos arquivos que antes não eram exibidos, existem dois diretórios especiais: `.` e `..`.

Estes diretórios são usados para nos referirmos a _Caminhos Relativos_ (Relative Paths). O diretório `.`, aponta para o diretório atual, onde a sessão do bash está localizada (o diretório onde você se encontra e que será exibido com o comando `pwd`).

Já o diretório `..`, aponta para o diretório pai do diretório atual, imediatamente superior na hierarquia de diretórios, o diretório que antecede o diretório atual na saída do comando `pwd`.

Ambos estes diretórios podem ser usados como atalho para execução de comandos, como os comandos que usamos até aqui:

```bash
# Criando alguns elementos para demonstrar caminhos relativos
cd ~
mkdir -p teste/a/b/c
cd teste/a/b
touch c/teste.txt

cp c/teste.txt .. # copia o arquivo dentro do diretório c para ~/teste/a
mv c/teste.txt . # move o arquivo dentro do diretório c para ~/teste/a/b
rm ../teste.txt # exclui o arquivo teste.txt do diretório ~/teste/a
cp teste.txt ../.. #copia o arquivo teste.txt do diretório atual para ~/teste
ls -lha ../.. # lista os arquivos do diretório ~/teste
```

Outro atalho útil para comandos usando o bash (e outros shells também costumam suportar), são _Caracteres Coringa_ (Wild Cards), usados para selecionar arquivos que correspondem com a alguns padrões em seus nomes. Para demonstrar isto, vamos antes criar alguns arquivos:
```bash
cd ~/teste
touch foo foo1 foo2 foo10 bar
```

Existem dois caracteres coringas: `?` e `*`.
- o `?` serve como uma forma de se referir a qualquer caractere que esteja em uma determinada posição no nome do arquivo. Por exemplo:
```bash
ls foo? # Lista todos os arquivos cujo nome começam com `foo` e que possuem qualquer outro caractere único em seguida
```

Note que, como resultado deste comando, os arquivos `foo1` e `foo2` foram os únicos exibidos. Os demais arquivos foram ignorados por não combinarem com o padrão, pois `foo` não possui nenhum caractere na posição onde o `?` se encontra, e `foo10` possui ainda um caractere a mais (já o arquivo `bar` não corresponde em absolutamente nada com o padrão usado).

- o `*` serve como uma forma de se referir a quaisquer combinação de zero ou mais caracteres que possam estar em uma determinada posição no nome dos arquivos. Por exemplo:
```bash
ls foo*
```

Desta vez, são listados todos os arquivos que começam com `foo`, independente de quantos caracteres a mais eles possuem ou não. O arquivo `bar`, como antes, é ignorado por não corresponder ao padrão.

Você pode usar os caracteres coringa para designar arquivos e diretórios como argumentos para qualquer comando do `Bash`. Por exemplo:
```bash
rm f?? # apaga somente o arquivo foo
cp foo* ./a # copia os arquivos foo1, foo2 e foo10 para ./a
mv foo? ./a/b # move somente os arquivos foo1 e foo2 para ./a/b
touch * # Atualiza a data/hora de modificação de todos os arquivos para a hora atual do sistema
```
