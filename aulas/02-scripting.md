# Aula 2 - Criando Scripts com Bash
Na aula passada fomos apresentados ao ambiente do Shell e começamos a nos familiarizar com a vida no terminal usando Bash. Apesar de termos explorado muitas ferramentas que nos permitem interagir com o sistema de arquivos, o uso do Shell não está relegado somente a manipular arquivos e diretórios. É possível usar o Shell como um ambiente produtivo para lidar com as mais diversas tarefas e, inclusive, automatizá-las.

Nesta aula iremos explorar as capacidades de automação do Bash e criar scripts que expandem a sua utilidade na execução de tarefas rotineiras, que o tornam, basicamente, uma linguagem de programação não muito diferente das muitas linguagens disponíveis.

## 2.1 - Imprimindo Valores (Hello world)
A operação mais básica que as linguagens de programação apresentam é a capacidade de imprimir um valor para o usuário. O ritual de iniciação padrão para todos os que estudam uma linguagem de programação é imprimir a mensagem universal "Hello, world" (_Olá mundo_). Usando Bash, o comando que usamos para imprimir mensagens para o usuário é o comando `echo`.

```bash
echo "Hello world"
```

Como vimos na aula passada, as aspas (`"`) são necessárias quando queremos usar espassos nos argumentos dos comandos que usamos no Bash, de outra forma o Bash iria interpretar os espaços como separadores de argumentos, possibilitando resultados inesperados. No caso do comando `echo`, independente de quantos argumentos você usa, o comportamento dele será o mesmo.

```bash
echo Hello world
```

Mas, é de bom tom seguir a convenção e usar delimitadores (`"` ou `'`) para garantir a consistência dos argumentos. Ao longo desta aula, manter esta consistência fará mais sentido, à medida que veremos como argumentos podem ser transformados ou reutilizados.

## 2.2 - Expressões
O uso de delimitadores, como o que usamos para definir o argumento "Hello world" para o comando `echo`, é um exemplo de uma _expressão_. Expressões são formas de criar valores em uma linguagem de programação, e em Bash não é diferente. Expressões de textos são as mais simples que podemos usar, mas existem outros tipos de expressões, e falaremos um pouco sobre alguns deles.

Um tipo de expressão comum em Bash, é o resultado da execução de um comando. Para criar expressões deste tipo, usamos a notação `$(<comando-bash>)`.

```bash
echo $(ls)
```

A linha acima executa o comando `ls` e usa a saída como resultado de uma expressão que é então passada para o comando `echo`. O resultado é semelhante à execução do comando `ls` no shell (a exibição da lista de arquivos). A diferença é que podemos usar esta expressão em outras operações, não apenas para exibí-las (usando o comando `echo`), mas também, por exemplo, atribuir este valor a variáveis e reutilizá-la para outros fins, como veremos em breve.

É possível, também, executar expressões aritméticas e exibir seu resultado. Para criarmos uma expressão aritmética, usamos a notação `$(( <expressão-aritmética> ))`. Desta forma, o shell não tentará interpretar a expressão como se fosse um comando.

```bash
echo $((7 + 8))
echo $((7 * 8))
echo $(((7 - 3) / (8 % 3)))
```

## 2.3 - Definindo variáveis
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

### 2.3.1 - Interpolação de Valores
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

### 2.3.2 - Variáveis Especiais pré-definidas
### 2.3.3 - Variáveis de ambiente
## 2.4 - Operadores
## 2.5 - Substituições de Comando 
## 2.6 - Expansões do Shell
## 2.7 - Stream de Erro
## 2.8 - Shell Script
### 2.8.1 - Executando Scripts
- shebang
### 2.8.2 - Estruturas de controle
### 2.8.3 - Funções
## 2.9 - Conclusão
