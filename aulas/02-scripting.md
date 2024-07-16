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

## 2.2 - Definindo variáveis
### 2.2.1 - Interpolação de Valores
### 2.2.2 - Variáveis Especiais pré-definidas
### 2.2.3 - Variáveis de ambiente
## 2.3 - Operadores
## 2.4 - Substituições de Comando 
## 2.5 - Expansões do Shell
## 2.6 - Stream de Erro
## 2.7 - Shell Script
### 2.7.1 - Executando Scripts
- shebang
### 2.7.2 - Estruturas de controle
### 2.7.3 - Funções
## 2.8 - Conclusão
