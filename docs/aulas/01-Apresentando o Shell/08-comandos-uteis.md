---
title: 1.8 - Comandos Úteis
---
- `man`
O comando `man` exibe um manual de diversos comandos do `bash`. Usa-se passando como argumento o nome do comando que se deseja consultar:
```bash
man mkdir
```

- `find`
O comando `find` ajuda a localizar arquivos, procurando não somente no diretório usado como argumento, mas automaticamente buscando em todos os seus subdiretórios. Se um diretório não for passado como argumento, o comando `find` usa o diretório atual por padrão. Ele aceita diversas opções para ajudar a encontrar arquivos de acordo com critérios específicos, como o nome do arquivo (opção `-name` seguido do nome que se busca, para usar coringas é necessário delimitar com apóstrofos), e muitas outras opções úteis.

Consulte o manual (`man find`) para ler sobre todas as opções disponíveis.

- `date`
Imprime a data/hora atual do sistema. Existem diversas opções de formatação em que a Data/Hora serão impressas, para saber mais consulte as páginas do Manual (`man date`)

- `diff`
Imprime as diferenças entre o conteúdo de dois caminhos, que precisam ser especificados via argumentos. Podendo ser ambos diretórios ou arquivos, mas não compara se forem de tipos diferentes.

- `history`
Imprime no terminal o histórico de comandos usados nesta sessão do `Bash`.

- `tail`
O comando `tail` é parecido com o comando `head`, com a diferença de que, em vez de tomar somente as primeiras x linhas da entrada e ignorar as demais, ele toma somente as últimas x linhas e ignora as primeiras.

- `less`
O comando `less` é ótimo para ser usado com comandos que resultam em um número elevado de linhas. Ele exibe o resultado de forma paginada e interativa, te permitindo controlar a navegação pelos dados.
