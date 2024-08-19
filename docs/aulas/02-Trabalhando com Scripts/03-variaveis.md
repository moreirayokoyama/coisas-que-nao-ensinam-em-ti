---
title: 2.3 - Definindo variáveis
---
Como em qualquer linguagem de programação, em Bash nós podemos definir variáveis para guardar valores que precisam ser reutilizados. Para definir variáveis em Bash, tudo o que precisamos fazer é uma atribuição de um valor a um nome, usando o operador `=`. O único cuidado que devemos ao fazermos uma atribuição é redobrar nossa atenção ao fato de que, em Bash, espaços contam. Por exemplo:

```bash
foo=bar # Atribuição do valor `bar` a uma nova variável chamada `foo`
foo = bar # Erro. O Bash tenta executar um comando chamado `foo` com 2 argumentos (`-` e `bar`).
```

Para usarmos as variáveis que criamos, nós nos referimos a elas usando o sinal `$` como prefixo. Por exemplo:

```bash
echo $foo
```

Qualquer resultado de uma expressão pode ser atribuído a uma variável:

```bash
soma=$((7 + 8))

```

## 2.3.1 - Interpolação de Valores
Interpolação de valores é a capacidade que o Bash tem de identificar marcadores em valores de texto para substituir por valores computados durante a execução do comando. Por exemplo:

```bash
echo "o conteúdo da variável foo é $foo"
```

No código acima, o Bash vai identificar o uso da variável foo (usada com o `$`), e vai substituir este marcador pelo valor da variável.

A interpolação de valores só funciona com textos delimitados por `"` (aspas). Se o texto for delimitado por `'` (apóstrofos), o bash trata o texto como literal e não faz a interpolação. Esta distinção tem suas vantagens, como por exemplo, quando você quer que a interpolação aconteça em um momento diferente do da execução do script, delegando a interpolação para outra etapa da automação, ou outro processo que será executado.

Podemos, também, interpolar valores resultantes de quaisquer tipos expressões suportadas pelo Bash.

```bash
echo "Interpolando o valor de uma variável: $foo"
echo "Interpolando o resultado de um comando: $(ls -lha ~ | grep Jul)"
echo "Interpolando o resultado de uma expressão aritmética: $((2 + 3 - 4 * 5 / 6 % 7))"
```

## 2.3.2 - Variáveis de ambiente
Variáveis de ambiente são valores que são carregados na sessão do shell e que ficam disponíveis para os programas e comandos que usamos ao longo desta sessão. Elas funcionam como qualquer outra variável definida no shell, com a diferença de que elas já estão criadas e disponíveis para serem usadas.

Uma forma de listar as variáveis de ambiente carregadas na sessão do shell é através do comando `export`.

```bash
export # Lista as variáveis de ambiente da sessão atual
```

Qualquer uma dessas variáveis podem ser usadas a partir de comandos no shell da mesma forma como as variáveis que definimos até aqui.

```bash
echo $HOME
echo $HOSTTYPE
echo "O diretório atual da sessão é $PWD, o diretório anterior é $OLDPWD"
```

Dentre as variáveis de ambiente, uma variável muito importante que afeta a forma como usamos o shell é a variável $PATH. Esta variável orienta o shell sobre em quais diretórios ele precisa buscar os programas que usamos. Por exemplo, quando usamos o programa `echo`, ou `grep`, ou outros programas que temos usado até aqui, o shell precisa saber como localizá-los e, para isto, usa a variável `$PATH`.

```bash
echo $PATH
```

Uma forma de saber onde está um dado programa que usamos é através do comando `which`.

```bash
which echo # imprime o endereço do programa echo
```

Com certeza, você irá encontrar o diretório exibido no caminho do comando `echo` como parte da variável `$PATH`, do contrário não seria possível usá-lo.

Para definir variáveis de ambiente na sessão do shell, também usamos o comando `export`, porém atribuindo o valor à variável que desejamos criar:

```bash
export foo=bar
x=y
export
```

Note que agora, entre as variáveis listadas, encontra-se a variável `foo` e seu valor. Por outro lado, a variável `x` não faz parte do ambiente, ela está carregada no shell, mas não é tratada como parte do ambiente.

## 2.3.3 O Ambiente
O _ambiente_ é uma lista de pares de `nome=valor` carregados na sessão do shell e que são fornecidos para os programas executados a partir daquela sessão. Isso é uma forma útil de fazer com que programas e scripts que executamos possam receber valores sem a necessidade de informá-los através de argumentos.

Veremos com mais detalhes como o ambiente funciona na [aula sobre o ambiente de linha de comando](../05-command-line-environment/index.md), quando discutiremos a execução de programas a partir do ambiente de linha de comando.

## 2.3.4 Sessões
Como acabamos de descrever, as variáveis de ambiente ficam disponíveis na sessão do Shell. A sessão do shell dura enquanto o shell estiver aberto. Se você sair do Bash, você encerra a sessão, e o ambiente daquela sessão deixa de existir.

Faça este teste, encerre o shell no terminal atual (fechando o terminal) e abra novamente o terminal. Uma nova sessão será criada e, se você executar o comando `export`, notará que a variável `foo` que acabamos de criar não está mais disponível.

As variáveis que você vê listadas através do comando `export` quando inicia uma nova sessão do shell são atribuídas ao ambiente durante a inicialização da sessão. Isto acontece graças a alguns scripts que são invocados no momento em que a sessão é iniciada.

Por exemplo, o script `~/.bashrc` possui a definição de diversas variáveis de ambiente. Outro arquivo útil é o `~/.profile` ou o `~/.profile_bash` (podem não existir no seu sistema, mas também são formas de definir o ambiente da sessão).

```bash
cat ~/.bashrc
cat ~/.profile
cat ~/.profile_bash
```

É interessante saber como o ambiente é criado na inicialização da sessão (através de arquivos como estes), para entendermos que todo o ambiente é facilmente configurável no shell, e que as coisas não acontecem como mágica.
