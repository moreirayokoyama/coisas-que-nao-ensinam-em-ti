---
title: 2.6 - Stream de Erro
---
Na aula passada nós falamos um pouco sobre os _streams_ que os programas recebem: o _stream de entrada_ e o _stream de saída_. Existe um terceiro stream que não mencionamos, que é o _stream de erro_. Ele designa ao programa que está sendo executado para onde as mensagens de erro serão enviadas.

Por padrão, o stream erro é o próprio terminal, como também é o padrão para o stream de saída.

```bash
mv zaz ~
```

Considerando que não exista um arquivo ou diretório chamado `zaz`, o comando acima irá gerar uma mensagem de erro e imprimir no terminal. Esta mensagem de erro foi escrita no stream de erro. Para observar isto, podemos religar o stream de saída a um arquivo e observar o comportamento do comando:

```bash
mv zaz ~ > zaz.out
cat zaz.out
```

Observer que, apesar de termos religado o stream de saída para o arquivo `zaz.out`, a mensagem de erro continua sendo exibida e o arquivo gerado está vazio. Isto demonstra como a mensagem gerada não foi produzida no stream de saída. Mas, como podemos religar o stream de erro a um arquivo? Podemos fazer isto através do operador `2>`:

```bash
mv zaz ~ > zaz.out 2> zaz.err
cat zaz.out
```

Desta vez a mensagem de erro não foi impressa no terminal, e o arquivo `zaz.err` foi criado, e ele contém a mensagem de erro que antes víamos impressa nos comandos anteriores. Desta forma podemos separar tanto o conteúdo escrito no stream de saída quanto o conteúdo escrito no stream de erro do terminal.
