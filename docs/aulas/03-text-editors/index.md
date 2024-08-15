---
title: Aula 03 - Explorando o Editor de Textos (Visual Studio Code)
description: Como usar um editor de texto como ferramenta produtiva para profissionais de TI
---
# Aula 3 - Explorando o Editor de Textos (Visual Studio Code)
Escrever um texto (como um documento, ou uma dissertação) e escrever código são atividades distintas. Quando se trabalha com código, você passa mais tempo navegando por ele, entre os diversos arquivos, lendo, interpretando e, claro, escrevendo código também. Não é à toa que existem ferramentas diferentes para este fim do que aquelas usadas para redigir um texto, como um processador de textos (por exemplo, o Microsoft Word do pacote Office). Processadores de Texto precisam suportar diversas opções de formatação (formatação de fonte, parágrafo, página, etc) que acabam sendo tão importantes quanto o prório texto sendo redigido.

Para trabalhar com código, usamos Editores de Textos. A diferença é que, em código, somente o conteúdo do texto importa. O arquivo mantido no sistema não possui informações de formatação. Não apenas esta informação não é relevante, como ainda não é suportada pelo código em si. Pense nos scripts que fizemos na aula passada, usando o comando `cat > foo.sh`, capturando os comandos que digitávamos no terminal e gravando no arquivo. Imagine se tivéssemos "comprometido" estes comandos com informações como "qual fonte usar", "qual tamanho do papel que será usado", etc.

Normalmente, quando trabalhamos com código, trabalhamos com arquivos de textos simples. Para ilustrar o que isso significa olhe para a imagem a seguir.

![image](/imagens/googledocs-helloworld.png)

Este é um Processador de Textos (Google Docs, similar ao Microsoft Word), com um texto  simples (o famoso "Olá Mundo!"). Mas se você tentar abrir o conteúdo salvo por este arquivo (no formato .doc) em um editor de textos, notará que existem muitas outras informações, a maior parte delas ilegível para um ser humano.

![image](/imagens/olamundo-doc-vscode.png)

Existe uma forma mais amigável de visualizar este arquivo, usando um decodificador Hexadecimal, mas isto não necessariamente o torna tão legível quanto um arquivo de texto.

![image](/imagens/olamundo-doc-hex.png)

Editores de texto, por outro lado, não interferem no conteúdo salvo pelo arquivo. Você pode escrever código direto no terminal como fizemos usando o comando `cat`, mas isto, provavelmente, vai ser pouco produtivo à medida que seus scripts começam a ficar mais complexos, já que o comando `cat` te dá poucas opções de edição.

Existem diversos editores de texto disponíveis. De fato, se você usa o sistema operacional Windows, você provavelmente possui instalado o Bloco de Notas (`notepad.exe`). Este é um editor de textos bastante rudimentar, que te permite criar arquivos de texto como os que usamos para manter código. Mas, justamente por que trabalhamos com código, existem opções ainda mais produtivas.

Existem diversos editores de texto feitos especificamente para trabalhar com código. Você vai encontrar profissionais que gostam de usar `Sublime Text`, ou o `Notepad ++` (que tem a proposta de ser um substituto para o Bloco de Notas do Windows com capacidades de produtividade com código), outros que vão preferir opções de editores de texto que rodam no terminal, como o `vim`, ou o `emacs`. E existem ainda ferramentas mais robustas, chamadas de _IDE_'s (_Integrated Development Environment_, ou, em português, Ambiente de Desenvolvimento Integrado), como o _Visual Studio_ da Microsoft, ou o _IntelliJ_ da JetBrains. Contudo, um editor específico mantém uma relevância significativa no mercado e, por que precisamos falar de alguma ferramenta, eu achei que a relevância do vscode não poderia ser ignorada.

De acordo com a pesquisa [_Stackoverflow Developer Survey_ de 2024](https://survey.stackoverflow.co/2024/technology#1-integrated-development-environment), de um total de mais de 58 mil entrevistados, 73,6% responderam que usam _vscode_ como o editor de código no dia-a-dia. Destes, mais de 44 mil usam profissionalmente, e mais de 6 mil o usam enquanto estão aprendendo a programar. Em ambos os casos, ele destaca sua adoção por mais do que o dobro do segundo colocado.

O vscode é mantido pela Microsoft, mas é um projeto de código aberto, mantido sob a licença MIT, e que recebe contribuição da comunidade.

!!! important
	É importante dizer que, na indústria, existe uma discussão acalorada sobre opções de editores de código, e vários grupos (principalmente entre as pessoas de programação) são muito opinativos a respeito da escolha por editores. A famosa discussão entre os usuários de _emacs_ e _vim_, tentando estabelecer um como superior ao outro, é um bom exemplo de como as pessoas defendem sua opção na indústria.

	Este curso não pretende estabeler o vscode como uma opção superior aos demais editores disponíveis. Apesar de ter capacidades de edição de código que não deixam a desejar (e em muitos casos, chega a ter uma excelente experiência de uso), a escolha pelo vscode se dá somente pela sua adoção e a presença que ele tem no mercado atualmente.

	Editores como Vim ou Emacs, além de não terem a mesma presença que o vscode tem na indústria, apesar de terem uma comunidade forte de usuários e mantenedores, também possuem uma curva de aprendizado (devido à natureza de como funcionam) que, na minha opinião, ainda que possuam suas vantagens, torna sua adoção uma opção indivudual de quem pretende explorá-los e, eventualmente, adotá-los como preferência.
