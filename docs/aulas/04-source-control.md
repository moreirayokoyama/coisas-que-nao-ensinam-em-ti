---
title: Aula 04 - Sistema de Controle de Versionamento de Código - Git
description: Usando um Sistema de Controle de Versionamento de Código como ferramenta de viagem no tempo e colaboração em projetos com código
---
# Aula 04 - Sistema de Controle de Versionamento de Código - Git
Trabalhar com código requer organização, e muito do que aprendemos sobre como organizamos o nosso código se dá com um trabalho iterativo e incremental, ou seja, o código está em constante mudança. Parte da nossa rotina no trabalho com código é de fazer, desfazer e refazer partes dele ao longo do desenvolvimento de uma tarefa, à medida que testamos e percebemos oportunidades de melhoria, ou até mesmo, problemas que não foram antecipados e que requerem mudanças na forma como havíamos elaborado a solução anteriormente.

Para ter algum controle sobre como estas alterações acontecem, e que possamos visualizá-las em um contexto histórico que torne essa organização possível, usamos um sistema de controle de versionamento de código. Existem diversas ferramentas para este fim disponíveis no mercado, mas uma delas se tornou um padrão de uso entre profissionais de TI nas últimas décadas: o Git.

O Git é um Sistema de Controle de Versionamento de Código (_SVC_), criado pelo Linus Torvalds enquanto ele desenvolvia o Kernel do Linux, disponível como software livre de código aberto sob a licença GPL, compatível com várias plataformas (Linux, MacOS e Windows). Ele é utilizado pela vasta maioria dos profissionais de tecnologia atualmente, tanto para projetos de Código Aberto quanto em organizações privadas.

Ele funciona através da criação de um repositório de código em um diretório no sistema de arquivos para acompanhar as mudanças que este código sofre ao longo do tempo. Neste repositório você é capaz de criar marcações do estado dos arquivos, e a partir destas marcações você tem a possibilidade de visualizar e navegar pelo histórico de como estes arquivos foram alterados, restaurar o estado em que eles se encontravam em um determinado momento no passado e reescrever a história deles a partir de uma marcação específica, além de diversas capacidades que veremos a seguir.

Nesta aula vamos explorar o uso de Git, tanto para organização pessoal, quanto para contribuição em projetos colaborativos.

## 4.1 - Instalando o Git
Para instalar o Git, basta acessar o [site oficial](https://git-scm.org), fazer o download para a plataforma do seu dispositivo e seguir as instruções de instalação.

- Linux

    A forma mais fácil de instalar Git no linux é através gerenciadores de pacotes. Usuários de Debian/Ubuntu, por exemplo, podem usar o `apt` para isto:

    ```bash
    sudo apt update
    sudo add-apt-repository ppa:git-core/ppa
    sudo apt install git
    ```

    Ele também está disponível para outros gerenciadores de pacote. Há uma [lista de gerenciadores suportados](https://git-scm.com/download/linux) no site oficial, ou você pode baixar o [tarball com o código fonte](https://mirrors.edge.kernel.org/pub/software/scm/git/) e seguir as instruções no arquivo `INSTALL`.

- macOS

    A forma mais fácil de instalar Git no macOS é instalando o Xcode Command Line Tools. A partir da versão 10.9, se você digitar qualquer comando git no Terminal pela primeira vez, você será perguntado se quier instalá-lo. Mas também é possível instalá-lo via _Homebrew_:

    ```bash
    brew install git
    ```

    Para consultar sobre outras formas de instalá-lo no macOS, acesse a [página com instruçoes detalhadas](https://git-scm.com/download/mac).

- Windows

    Existe uma [página com os downloads para Windows](https://git-scm.com/download/win). Como de praxe, o processo de instalação é assistido por algumas etapas exibidas pelo instalador. Durante estas etapas, descrevemos aqui alguns ajustes importantes que precisam ser feitos durante o processo:
    - Na etapa _**Select Components**_, você pode achar interessante se certificar de que a opção "_Add a Git Bash Profile to Windows Terminal_" está marcada.
    ![image](../imagens/git-selectcomponents.png)
    
    - Na etapa _**Choosing the default editor used by Git**_, você pode escolher o Visual Studio Code.
    ![image](../imagens/git-choosingeditor.png)

    - Na etapa _**Adjusting the name of the initial branch in new repositories**_, é de bom tom marcar a opção "_Override the default branch name for new repositories_" e preencher o campo de texto com `main`. Isto se dá por que o nome da branch padrão na instalação do git é visto como uma palavra que pode ser ofensiva para grupos minoritários, e `main` tem sido a alternativa inclusiva usada pela comunidade.
    ![image](../imagens/git-defaultbranchname.png)

        - Importante dizer que os próprios mantenedores do Git [pretendem mudar isto](https://sfconservancy.org/news/2020/jun/23/gitbranchname/) em algum momento no futuro. Mas enquanto a discussão de como isto será implementado definitivamente continua em progresso, eles já dispoinibilizaram a opção para fazer este ajuste manualmente.

    - Na etapa _**Adjusting your PATH environment**_ é recomendável selecionar ao opção "_Git from the command line and also from 3rd-party-software_", que faz com que o Git possa ser usado tanto através do _Git Bash_, quanto também a partir dos Shells do Windows, colocando o CLI do Git como parte do PATH nas variáveis de ambiente do Windows.
    ![image](../imagens/git-pathenvironment.png)

    - Na etapa _**Choosing the SSH executable**_ é recomendável manter a primeira opção selecionada, "_Use bundled OpenSSH_". Isso te poupa de ter que usar uma outra ferramenta de _SSH_ (falaremos mais de SSH durante o curso).
    ![image](../imagens/git-choosessh.png)

    - Na etapa _**Choosing HTTPS transport backend**_, é recomendável manter a primeira opção selecionada, "_Use the OpenSSL library_". Você só vai precisar escolher a outra opção ("_Use the native Windows Secure Channel Library_") se você estiver trabalhando em uma empresa ou em uma organização que gerencie seus prórios certificados.

    - Na etapa _**Configuring the line ending conversions**_, selecione "_Checkout as-is, commit Unix-style line endings_. Esta opção tem a ver com como o git irá lidar com a compatibilidade do formato da quebra-de-linha. Por padrão, o git usa o estilo do Unix como símbolo para quebra de linhas, o _Line Feed_ (`LF`). Mas o Windows trabalha de forma diferente: _Carriage Return_ e _Line Feed_ (`CRLF`). Nós falamos um pouco sobre isso na [Aula sobre vscode](./03-text-editors.md).
    ![image](../imagens/git-lineending.png)

    As demais opções podem ser mantidas com o valor padrão.

    Após a instalação, abra um Shell do Windows no terminal e digite o seguinte comando:

    ```cmd
    git --version
    ```

    Se o git estiver devidamente instalado, uma mensagem comunicando a versão do git será exibida. Se uma mensagem de erro for exibida no lugar, você precisa rever o processo.

!!! Importante

    Se você usa Windows, mas está acompanhando o curso pelo _WSL_, você precisa efetuar a instalação do Git no WSL, seguindo os passos de instalação no Linux.

- Configurando a instalação do Git
    
    Agora que temos o git instalado, precisamos fazer algumas configurações iniciais antes de começarmos a usá-lo. A primeira é configurar os seus dados, que serão usados pra te identificar quando você começar a usá-lo para acompanhar as alterações que você faz nos seus projetos.

    Para isto usamos o comando `git config`, e parametrizamos as configurações `user.name` e `user.email`. Mas faremos isso como configuração global, usando a flag `--global`. O Git permite você ter ajustes globais que funcionarão para todos os repositórios por padrão, embora você também possa alterar as alterações específicas em cada repositório. Por exemplo, em repositórios de projetos para organizações específicas você pode preferir configurar seu e-mail naquela organização.

    ```bash
    git config --global user.name "Tio Dani" # Configura a forma como você quer ser identificado
    git config --global user.email "mail@tiodani.com" # Configura o seu e-mail
    ```

Tudo pronto. Agora que temos o git devidamente instalado e configurado, podemos finalmente começar a brincar com ele. É o que faremos a seguir.

## 4.2 - Iniciando um Repositório
Vamos agora entender como começamos a trabalhar com Git. O primeiro conceito que precisamos aprender sobre Git é o Repositório (informalmente chamado de _repo_). Sempre que você quiser trabalhar com o Git, você vai precisar criar um repositório. Um repositório é, de certa forma, um repositório no seu sistema de arquivos. Isto é conveniente, já que normalmente nós colocamos usamos diretórios como forma de organizar nossos projetos, então é natural que pensemos que, toda vez que criamos um diretório para trabalhar em um projeto, este mesmo diretório é um candidato em potencial para se tornar o repositório Git daquele projeto.

Se você já tem um projeto em andamento ou se vai começar um do zero, não importa, para criar um repo você só precisa entrar na pasta e iniciar o repositório:

```bash
mkdir novo_projeto && cd novo_projeto
git init
```


- git init
- git status
- git add 
- git commit
- git restore
- git reset
## 4.3 - Navegando pelo histórico de alterações
- git log
- git show
- git diff
- git checkout
- git reset
- git tag
## 4.4 - Trabalhando com Branches
- git branch
- git switch
- git checkout
## 4.5 - Merge
- git merge
- Conflitos
## 4.6 - Repositórios Remotos
- clone
- fetch
- pull
- push
## 4.7 - Serviços de Colaboração - CodeBerg
- fork
- Pull request
## 4.8 - Rebase
- git rebase


