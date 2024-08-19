---
title: 1.7 - Conectando Programas
---
Uma das capacidades mais incríveis do `Bash` é a forma como é possível manipular a entrada e saída dos programas e conectá-las de diversas formas para redefinir o comportamento padrão dos comandos. Me permita explicar melhor antes, como o Shell lida com a entrada e saída dos comandos.

## 1.7.1 Streams de Entrada e Saída (Input/Output Streams)
No Shell, programas possuem dois _streams_ primários associados a eles: o stream de _entrada_ (input), e o stream de _saída_ (output). Quando o programa tenta ler a entrada, ele lê do stream de entrada, e quando ele imprime algo, ele imprime no stream de saída. Normalmente, os streams de entrada e saída de um programa são o seu terminal (quando rodando a partir do shell). Ou seja, seu teclado (à medida que você digita no shell) e a janela do terminal na sua tela. Contudo, nós podemos também religar estes streams de outras formas.

!!! important
	 **Streams** em computação, é um termo comum usado para designar um fluxo de dados que não acontece de uma única vez, mas que é feito de forma contínua, ao longo do tempo, em pequenos lotes.

	 Aqui estamos falando de Streams sendo usados para o fluxo contínuo de dados de entrada e de saída de um comando ou programa executado no shell. Mas o conceito é muito comum em diversas outras áreas da computação, como na leitura/escrita de arquivos no disco, ou obtendo/enviando dados através da rede/internet.

	O termo ficou ainda mais popular com a transmissão de conteúdo online como chamadas de vídeo ou transmissões audiovisuais em _lives_ na internet.

## 1.7.2 Religamento de Streams
A forma mais simples de religar streams no `Bash` é através dos operadores `>` (para religar o stream de saída do programa) e `<` (para religar o stream de entrada do programa). Vamos ver alguns exemplos:

```bash
ls ~ -lha > ~/teste/ls.txt # Religa o stream de saída do comando ls para o arquivo ~/teste/ls.txt
```

Note que o comando `ls` acima não imprimiu a saída no terminal como de costume. Por outro lado, você pode conferir um novo arquivo criado no diretório `~/teste` chamando `ls.txt`. Você pode usar o comando `cat` (que imprime o conteúdo de um arquivo no terminal) e você irá notar que o seu conteúdo é a saída do comando `ls` que teria sido impressa no terminal se não a tivéssemos religado.

Uma forma de conferir o conteúdo do arquivo `~/teste/ls.txt`, é o utilizando como stream de entrada do comando `cat`, que imprime o stream de entrada no stream de saída. Ao religar o stream de entrada do comando `cat` usando o arquivo `~/teste/ls.txt` sem religar o stream de saída, ele irá imprimir o conteúdo no terminal.

```bash
cat < ~/teste/ls.txt
```

O comando `cat`, quando não especificado nenhum argumento, usa o terminal como stream de entrada (capturando tudo o que o usuário digitar) e as imprime no stream de saída (que também é o próprio terminal, imprimindo exatamente o que é digitado), à medida que os dados são enviados (normalmente, sempre que uma linha é finalizada). O resultado padrão do comando `cat`, é ter suas linhas repetidas, uma vindo pela entrada, e logo em seguida sendo impressa na saída.

```bash
cat # demonstrando os dados digitados no stream de entrada, e impressos na saída imediatamente depois
```

Por exemplo, é possível usar o cat como um editor de um novo arquivo, que será criado usando a religação do stream de saída, digitando o conteúdo a partir do stream de entrada.

```bash
cat > ~/teste/arquivo.txt # Ao digitar conteúdo na entrada, ele será direcionado para o arquivo.txt
```

!!! note
	Para encerrar a leitura da entrada, nós usamos o comando Ctrl+C. Isto envia um sinal para o processo que está executando o comando `cat`, orientando-o a parar.

	Existem outras formas de enviar sinais aos processos quando estamos executando programas no bash, mas veremos isto no futuro.

Um outro operador útil é o operador `>>`. Ele tem, basicamente o mesmo efeito do operador `>`, que religa o stream de saída, com exceção de que, se a saída é redirecionada a um arquivo que já existe, ele concatena a saída do programa atual ao conteúdo original do arquivo, uma operação popularmente conhecida na computação como `append`. Ou seja, o conteúdo original do arquivo é mantido, e o novo conteúdo é enviado ao final dele.

```bash
ls -lha ~ >> ~/teste/arquivo.txt
```

Note que o conteúdo original do `arquivo.txt` foi mantido, e o resultado do comando `ls` foi inserido depois da última linha original.

Existe um operador que conecta a saída de um comando do bash à entrada de outro comando, criando uma cadeia de comandos, ou "esteira" (_pipeline_), de etapas pelas quais os dados resultantes de um programa são aplicados ao outro, sendo transformados até produzirem uma saída desejada. Este operador é o `|` (_pipe_).

```bash
ls -lha ~ | grep Jul | head -5 | tee /home/dmyoko/teste/pipeline.txt
```

Aqui temos uma pipeline que faz a seguinte sequência:
- `ls -lha ~` - lista todos os arquivos da pasta `home`, em formato de lista, com tamanhos humanamente legíveis, e inclindo os arquivos ocultos (que começam com `.`)
- `grep Jul` - o comando `grep` filtra as linhas vindas da entrada de acordo com algum padrão (no caso, `Jul`). Basicamente ele pega o resultado do `ls` e separa somente os arquivos modificados em Julho
- `head -5`- O comando `head` toma somente as primeiras linhas da entrada. Por padrão, ele toma somente as primeiras 10, mas a opção `-5` faz com que ele pegue somente as primeiras 5 e ignore as demais linhas.
- `tee /<caminho>` - O comando `tee` é um comando similar ao comando `cat`, com a diferença que, além de imprimir no stream de saída, ele também escreve o arquivo. No caso acima, ele escreve no terminal e no arquivo `/home/dmyoko/teste/pipeline.txt`.
	- Por exemplo, é possível criar dois arquivos a partir do comando `tee`:

```bash
ls -lha ~ | grep Jul | head -5 | tee /home/dmyoko/teste/pipeline.txt > /home/dmyoko/teste/pipeline2.txt
```

- A linha acima instrui instrui o `tee` a escrever a entrada no arquivo `/home/dmyoko/teste/pipeline.txt` e religa o stream de saída para o arquivo `/home/dmyoko/teste/pipeline2.txt` usando o operador `>`.
- Imagine talvez, usar o operador `>>` nesta linha, e qual será o resultado. Como isso iria diferir ambos os arquivos.

Nós iremos usar muito o operador de pipe (`|`) na aula em que iremos tratar de _Manipulação de Dados_ no Shell.
