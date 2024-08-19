---
title: 1.5 - Manipulação do sistema de arquivos
---
Agora que sabemos como navegar e obter informações sobre o conteúdo do sistema de arquivos, vamos aprender como manipular o conteúdo dos diretórios, criando, modificando e excluindo arquivos e diretórios usando comandos do Shell.

- Criando diretórios: `mkdir`

Para criar novos diretórios, usamos o comando `mkdir` passando como argumento o nome  do diretório que queremos criar.

```bash
cd ~ #Certifique-se de estar no seu diretório `home`
mkdir teste
```

O diretório `teste` será criado no diretório atual, no caso, o diretório `home`. Você também pode criar um diretório em um lugar diferente do diretório atual, usando o endereço completo desejado.

```bash
mkdir /home/dmyoko/teste/tmp
```

!!! warning
	**Espaços importam!** Tome cuidado com o uso de espaços quando estiver executando operações no shell. Por exemplo, se você digitar o comando `mkdir minhas fotos`, ao invés de criar um diretório chamado `minhas fotos`, ele irá criar dois diretórios, um chamado `minhas` e um segundo chamado `fotos`. Para usar espaços você pode usar caracteres de escape.

Para usar caracteres de escape, você usa a `\` (barra invertida). Por exemplo:
```bash
mkdir Minhas\ Fotos # Cria um diretório chamado `Minhas Fotos`
```

Você pode, também, delimitar o nome usando aspas (`"`) ou apóstrofos (`'`), como uma forma de indicar o nome sem usar caracteres de escape.

O comando `mkdir` possui uma opção `-p` que permite que você crie um caminho completo de diretórios:

```bash
mkdir -p /home/dmyoko/teste/a/b/c
```

Note que ele sabe lidar com o fato de que parte do caminho já existe (o diretório `/home/dmyoko/teste/`), e cria apenas os segmentos que não existem.

Uma outra conveniência desta opção é que ela não resulta em erro, caso você tente criar um diretório que já existe, mesmo que seja o caminho completo. Isto é útil, principalmente para automações.

```bash
mkdir /home/dmyoko/teste/a/b/c #Resulta em erro
mkdir -p /home/dmyoko/teste/a/b/c
```

- Manipulando hora de acesso e modificação de arquivos: `touch`

O comando touch força uma alteração na data de modificação de arquivos.

Para entender o que isto significa, vamos rever o resultado do comando `ls` no screenshot anterior:
![image](../../imagens/permissoes-ls-l.png)

Observe a coluna imediatamente à esquerda do nome do arquivo nesta lista, é uma informação de Data/Hora. Esta coluna indica a data/hora da última modificação que este arquivo teve. Ao usar o comando `touch`, você força uma atualização desta informação para a data/hora atual do sistema.

Apesar disso parecer algo usado para um propósito muito específico, o comando `touch` é útil por que, ao ser usado para fazer isto em um arquivo inexistente, ele cria o arquivo. Por exemplo:

```bash
touch teste.txt
```

Se o arquivo teste.txt não existir, ele será criado. Caso ele exista, somente a data/hora da última modificação serão afetados. Isto é útil quando trabalhamos com scripts de automação, pois garante a existência do arquivo sem incorrer num erro ao tentar criá-lo novamente ou substituí-lo acidentalmente.

- Copiando arquivos com `cp`

O comando `cp` é usado para copiar arquivos. Ele funciona com dois argumentos:
- O primeiro argumento é o caminho do arquivo de origem, que se deseja copiar
- O segudno argumento é o caminho do arquivo de destino, para onde se deseja copiar o arquivo de origem

Por exemplo:

```bash
cp teste.txt teste2.txt
cp /home/dmyoko/teste /home/dmyoko/teste2 #Funciona com diretórios
```

- Movendo arquivos com `mv`

Por outro lado, se a intenção é apenas mover arquivos entre caminhos, em vez criar uma cópia (fazendo com que o arquivo deixe de existir no caminho de origem), o comando `mv` pode ser usado de forma semelhante ao `cp`, passando os mesmos argumentos.

```bash
mv teste2.txt teste3.txt #Funciona como se o arquivo fosse renomeado
mv teste3.txt /home/dmyoko/teste2
mv /home/dmyoko/teste2 /home/dmyoko/teste3
```

- Removendo arquivos com `rm`

Para remover arquivos, usamos o comando `rm`. Ao contrário dos comandos anteriores `cp` e `mv`, o comando `rm` não afeta diretórios por padrão. Sendo usado especificamente para arquivos.

Por exemplo:
```bash
rm /home/dmyoko/teste/teste3.txt
```

Para remover diretórios, existe o usando o comando `rmdir`, mas ele funciona apenas com diretórios vazios. Se houve qualquer arquivo dentro do diretório, ele se recusa a excluí-lo. Por exemplo:

```bash
rmdir /home/dmyoko/teste
```

Gera esta mensagem de erro:
```
rmdir: failed to remove 'teste': Directory not empty
```

Para remover um diretório não vazio (excluindo seu conteúdo em consequência), o comando `rm` disponibiliza opções que permitem fazer isto. O motivo de exigir o uso destas opções é evitar que se exclua arquivos por acidente, forçando o usuário a fazer o uso deliberado delas para se certificar do que está fazendo.

```bash
rm -r /home/dmyoko/teste
```
