---
title: Aula 03 - Explorando o Editor de Textos (VSCode)
description: Como usar um editor de texto como ferramenta produtiva para profissionais de TI
---
# Aula 3 - Explorando o Editor de Textos (Visual Studio Code)
Escrever um texto (como um documento, ou uma dissertação) e escrever código são atividades distintas. Quando se trabalha com código, você passa mais tempo navegando pelo texto, ou entre arquivos, lendo e interpretando código e, claro, escrevendo código também. Não é à toa que existem ferramentas diferentes para este fim do que aquelas usadas para redigir um texto, como um processador de textos (por exemplo, o Microsoft Word do pacote Office). Processadores de Texto precisam suportar diversas opções de formatação (formatação de fonte, parágrafo, página, etc) que acabam sendo tão importantes quanto o prório texto sendo redigido.

Para trabalhar com código, usamos Editores de Texto. A diferença é que, em código, somente o texto importa. O arquivo mantido no sistema não possui informações de formatação. Não apenas esta informação não é relevante, como ainda não é suportada pelo código em si. Pense nos scripts que fizemos na aula passada, suando o comando `cat > foo.sh`, capturando os comandos que digitávamos no terminal e gravando no arquivo. Imagine se tivéssemos "comprometido" estes comandos com informações como "qual fonte usar", "qual recuo da margem", etc.

Normalmente, quando trabalhamos com código, trabalhamos com arquivos de textos simples. Para ilustrar o que isso significa olhe para a imagem a seguir.

![image](../imagens/googledocs-helloworld.png)

Este é um Processador de Textos (Google Docs, similar ao Microsoft Word), com um texto  simples escrito (o famoso "Olá Mundo!"). Mas se você tentar abrir o conteúdo salvo por este arquivo (no format .doc) em um editor de textos, notará que existem muitas outras informações, a maior parte delas ilegível para um ser humano.

![image](../imagens/olamundo-doc-vscode.png)

Existe uma forma mais amigável de visualizar este arquivo, usando um decodificador Hexadecimal, mas isto não necessariamente o torna tão legível quanto um arquivo de código.

![image](../imagens/olamundo-doc-hex.png)

Editores de texto, por outro lado, não interferem no conteúdo salvo pelo arquivo. Você pode escrever código direto no terminal como fizemos usando o comando `cat`, mas isto provavelmente vai ser pouco produtivo à medida que seus scripts começam a ficar mais complexos, já que o comando `cat` te dá poucas opções de edição.

Existem diversos editores de texto disponíveis. De fato, se você usa o sistema operacional Windows, você provavelmente possui instalado o Bloco de Notas (`notepad.exe`). Este é um editor de textos bastante rudimentar, que te permite criar arquivos de texto como os que usamos para manter código. Mas, justamente por que trabalhamos com código, existem opções ainda mais produtivas.

Existem diversos editores de texto feitos especificamente para trabalhar com código. Você vai encontrar profissionais que gostam de usar `Sublime Text`, ou o `Notepad ++` (que tem a proposta de ser um substituto para o Bloco de Notas do Windows com capacidades de produtividade com código), outros que vão preferir opções de editores de texto que rodam no terminal, como o `vim`, ou o `emacs`. E existem ainda ferramentas mais robustas, chamadas de _IDE_'s (_Integrated Development Environment_, ou, em português, Ambiente de Desenvolvimento Integrado), como o _Visual Studio_ da Microsoft, ou o _IntelliJ_ da JetBrains. Contudo, um editor específico mantém uma relevância significativa no mercado e, por que precisamos falar de alguma ferramenta, eu achei que a relevância do Visual Studio Code não poderia ser ignorada.

De acordo com a pesquisa [_Stackoverflow Developer Survey_ de 2024](https://survey.stackoverflow.co/2024/technology#1-integrated-development-environment), de um total de mais de 58 mil entrevistados, 73,6% responderam que usam _VSCode_ como o editor de código no dia-a-dia. Destes, mais de 44 mil usam profissionalmente, e mais de 6 mil o usam enquanto estão aprendendo a programar. Em ambos os casos, ele destaca sua adoção por mais do que o dobro do segundo colocado.

O VSCode é mantido pela Microsoft, mas é um projeto de código aberto, mantido sob a licença MIT, e que recebe contribuição da comunidade.

!!! important
    É importante dizer que, na indústria, existe uma discussão acalorada sobre opções de editores de código, e vários grupos (principalmente entre as pessoas de programação) são muito opinativos a respeito da escolha por editores. A famosa discussão entre os usuários de _emacs_ e _vim_, tentando estabelecer um como superior ao outro, é um bom exemplo de como as pessoas defendem sua opção na indústria.

    Este curso não pretende estabeler o VSCode como uma opção superior aos demais editores disponíveis. Apesar de ter capacidades de edição de código que não deixam a desejar (e em muitos casos, chega a ter uma excelente experiência de uso), a escolha pelo VSCode se dá somente pela sua adoção e a presença que ele tem no mercado atualmente.

    Editores como Vim ou Emacs, além de não terem a mesma presença que o VSCode tem na indústria, apesar de terem uma comunidade forte de usuários e mantenedores, também possuem uma curva de aprendizado (devido à natureza de como funcionam) que, na minha opinião, ainda que possuam suas vantagens, torna sua adoção uma opção indivudual de quem pretende explorá-los e, eventualmente, adotá-los como preferência.

## 3.1 Instalando o VsCode

Para instalar o VSCode, que roda na maioria das plataformas disponíveis, basta visitar o [site oficial](https://code.visualstudio.com), e se dirigir à página de downloads e clicar no link adequado de acordo com o seu sistema.

![image](../imagens/vscode-download.png)

A partir daí, basta seguir as [instruções](https://code.visualstudio.com/docs/setup/setup-overview).

!!! Important
    Para instalações no Windows, é importante lembrar-se de manter marcado a opção "Add to PATH" (Adicionar para o PATH). Isso torna o _code_ fácil de iniciar a partir do _shell_, inclusive para quem usa o WSL, como recomendado neste curso.

    ![image](../imagens/vscode-install-windows.png)

## 3.1 Explorando a interface
Ao abrir o Visual Studio Code, uma página de boas-vindas é exibida como uma aba aberta na janela do editor, muito semelhante a que você pode enxergar abaixo, com algumas diferenças de acordo com o seu uso (na minha, é possível ver alguns dos meus projetos recentes listados, prontos para serem abertos).

![image](../imagens/code.png)

A partir desta página, algumas tarefas comuns já estão acessíveis, como criar um novo arquivo, abrir um arquivo existente, abrir um diretório, e até mesmo clonar um repositório _git_. É possível, também, se conectar a outros ambientes, como o WSL, ou remotamente via SSH e outras opções.

Do lado direito, você pode ver alguns guias (_Walkthroughs_), que podem te ajudar a se familiarizar com a interface e o uso do _code_.

No topo da interface, como já é típico de aplicações que rodam em interface gráfica, temos uma barra de menus, com alguns dos menus mais conhecidos, como _Arquivo_, _Editar_ e _Ajuda_. Como esperado, o menu _Arquivo_ exibe mais opções relacionadas a manipulação de arquivos, _Editar_ tem opções úties como _Copiar_, _Colar_, além de outras conveniências de edição, e o menu _Ajuda_, sem nenhuma surpresa, trás informações úteis para quem precisa de algum suporte.

À esquerda, temos a Barra Lateral, com algumas funcionalidades dispostas de forma conveniente, como _Explorador de Arquivos_, _Busca_, _Controle de Código_, o _Depurador_ e o painel de _Extensões_.

Mais abaixo, ainda na _Barra Lateral_, existem as opções de _Configurações_, onde você pode personalizar o _Code_ de acordo com as suas preferências, por exemplo, sua preferência por um tema claro ou escuro (e outras combinações de cores) pode ser ajustada ali. E também existe a opção de usar uma conta (na Microsoft ou no Github) para associar ao seu uso, o que pode ser útil, por exemplo, para manter suas configurações salvas e poder usá-las em um _Code_ instalado em outro computador.

## 3.2 Editor

### 3.2.1 Trabalhando com arquivos
Comentários
---

Mover texto
---

Copiar texto
---

Cursores
---

Seleção de coluna
---

### 3.2.2 Abas
### 3.2.3 Modos de Linguagem
### 3.2.4 Quebra de linha
### 3.2.5 Indentação
### 3.2.6 Aparência
### 3.2.7 Layout
<!-- Menu Go -->
### 3.2.8 Navegação
## 3.3 Barra lateral
### 3.3.1 Explorador de Arquivos
### 3.3.2 Busca
### 3.3.3 Extensões
## 3.4 Painel
### 3.4.1 Problemas
### 3.4.2 Saída
### 3.4.3 Console de depuração
### 3.4.4 Terminal