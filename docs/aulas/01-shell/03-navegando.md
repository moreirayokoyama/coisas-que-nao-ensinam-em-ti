---
title: 1.3 - Navegando com o Shell
---
Vamos começar a explorar os comandos do Bash, aprendendo primeiro a navegar pelo sistema de arquivos.

- Exibindo o diretório atual: `pwd`

Como vimos agora há poudo, o comando `pwd` (_Print Working Directory_), imprime no terminal o caminho do diretório atual onde o Shell irá executar o próximo comando. Saber qual é o diretório atual é importante, por que isto pode afetar diretamente o resultado do próximo comando.

Por exemplo, se o próximo comando resultar na criação de um arquivo, o arquivo será criado no diretório atual, exceto se algum parâmetro específico seja usado para mudar este comportamento (salvo, é claro, se o programa executado tiver instruções específicas do caminho do arquivo).

- Mudando o diretório atual: `cd`

Para mudar o diretório atual da sessão do Shell, o comando usado é o `cd` (_Change Directory_). Se você digitar apenas `cd` e pressionar Enter, ele vai mudar o diretório atual para `~` (falaremos logo a seguir sobre que diretório é este). Ele não imprime nenhuma saída, e imediatamente um novo prompt é apresentado. Para informar o comando `cd` para que ele mude para um diretório diferente, um `argumento` precisa ser usado.

!!! note
	**Argumentos**: são complementos que damos aos comandos, normalmente digitando-os a seguir do comando propriamente dito. Por exemplo, no comando `cd teste`, `teste` é o argumento passado para o comando `cd`. Neste caso, o comando `cd` vai mudar mudar o diretório atual para o diretório `teste`.

```bash
cd teste
```

No meu caso, uma mensagem de erro é exibida:

```
bash: cd: teste: No such file or directory
```

Ela diz que não existe um arquivo ou diretório chamado `teste`. Note, executando o comando `pwd` novamente, que o diretório atual permanece o mesmo.

Para mudar o diretório atual, precisamos passar como argumento, o endereço de um diretório existente. Por exemplo, um diretório que com certeza existe no sistema de arquivos é o diretório raiz, que fica no endereço `/`.

```bash
cd /
```

No meu caso, como você pode ver, o meu prompt mudou, agora dizendo que o diretório atual é `/` (o diretório raiz). Se o seu prompt não exibe esta informação como o meu, você pode confirmar usando o comando `pwd`.

Outro diretório comum para quem usa o Bash, é o diretório _Home_, representado pelo caractere `~`. Você pode testar o comando:

```bash
cd ~
```

Como pode ver, no meu prompt, agora ele exibe `~` como diretório atual, e não mais o diretório raiz (`/`).

Ao contrário do diretório raiz, se você usar o comando `pwd` agora você vai notar que o diretório _Home_ (`~`), na verdade, aponta para um diretório específico a partir da raiz. No meu caso, `/home/dmyoko` (no seu caso, vai apontar para um diretório com o nome do seu usuário dentro do diretório `/home`).

Você pode navegar manualmente por estes diretórios, usando o caminho que os leva até eles. Por exemplo:

```bash
cd /
cd home
cd dmyoko
```

Uma vez no diretório `/` (raiz), você tem acesso ao diretório `home`, e uma vez que você entra no diretório `home`, você tem acesso ao diretório do seu usuário, no meu caso `dmyoko`.

Você também pode navegar direto para o diretório específico, usando o caminho completo absoluto que leva até ele, começando pelo diretório raiz.

```bash
cd /
cd /home/dmyoko
```

!!! note
	**Caminho absoluto** é o caminho completo que leva até um diretório ou arquivo no sistema de arquivos. Ele sempre começa pelo diretório `/` (raiz), e segue toda a hierarquia de segmentos necessários até chegar no diretório ou arquivo desejado.

- Listar informações sobre o conteúdo de um diretório: `ls`

O comando `ls` é útil quando você deseja entender o conteúdo de um determinado diretório. Se você digitar somente `ls`, o Bash imprimirá no terminal o conteúdo do diretório atual.

Se você quiser listar o conteúdo de outro diretório sem necessariamente sair do diretório atual, basta usar como argumento o caminho para o diretório do qual você pretende listar o conteúdo desejado.

```bash
ls /
```

O comando acima, lista o conteúdo do diretório `/` (raiz). Você pode também listar o conteúdo de um dos subdiretórios do diretório raiz, informando o endereço dele. Por exemplo:

```bash
ls /bin
ls /lib
ls /sys/devices/cpu
```

O comando `ls` também suporta opções, que podem influenciar no resultado do comando. Por exemplo, a opção `-l` exibe o resultado do comando `ls` no formato de lista, trazendo informações adicionais a respeito do conteúdo do diretório, que antes não estavam sendo exibidas, como as [permissões de acesso](#24-permissoes-de-arquivos-e-diretorios) ao diretório/arquivo listado, informações de quem é o usuário dono deste diretório/arquivo e a que grupo ele pertence (usuário `dmyoko` do grupo `dmyoko`, por exemplo), o tamanho do arquivo/diretório em bytes, e a data da última vez que o arquivo/diretório foi modificado.

```bash
ls -l
```

Outra opçõa útil é o `-h`, que faz com que os tamanhos dos arquivos exibidos sejam impressos num formato _humanamente legível_ (human readable).

```bash
ls -h # sem efeito, pois os tamanhos não são exibidos
ls -l -h # agora é possível ver o efeito.
ls -lh # é possível unir todas as opções em uma única cláusula
```

Existem outras diversas opções disponíveis para o comando `ls`. Para ter acesso a uma lista completa delas, você pode digitar `ls --help`.

!!! tip
	`--help` é uma opção disponível na vasta maioria dos comandos que você pode executar no shell. E, invariavelmente, imprime informações sobre o que o comando faz e como utilizá-lo, inclusive, mostrando possíveis opções que afetam a forma como este comando se comporta.
