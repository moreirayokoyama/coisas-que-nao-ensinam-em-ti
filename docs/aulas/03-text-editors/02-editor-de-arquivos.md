---
title: 3.2 - O Editor
---

Agora vamos explorar o uso do vscode para o que ele se propõe: Editar arquivos.

Vamos começar criando um novo arquivo. Isto pode ser feito de diversas formas:
- Clicando em _New File..._ na página de _Welcome_
- Clicando no Menu _File_, e escolhendo a opção _New Text File_
- Usando as teclas de atalho _Ctrl+N_

Um novo arquivo, sem título, será aberto em uma nova Aba dentro da janela do editor. Um texto é exibido como conteúdo deste arquivo, dizendo que você pode "Selecionar uma Linguagem" (_Select a language_), "Preencher um Template" (_fill with template_) ou "Abrir um Editor Diferente" (_open a different editor_). Logo abaixo, o texto também explica que, se você começar a digitar algum conteúdo, esta mensagem irá desaparecer, e você pode também optar por não exibí-la novamente nas próximas vezes em que criar um novo arquivo (_don't show this again_).

![image](../../imagens/vscode-newfile.png)

Selecionar uma linguagem, significa mudar o modo de linguagem do arquivo no qual estamos trabalhando. É possível fazer isto clicando no link do texto, ou também no seletor do modo de linguagem, que fica na barra de status (na borda inferior da janela do vscode), à direita. Ela começa com a opção "Plain Text" selecionada, mas é possível mudá-la clicando sobre ela, e um menu suspenso será exibido nos permitindo selecionar a linguagem que pretendemos usar. Vamos selecionar "Shell Script", que é o tipo de arquivo com o qual estamos trabalhando atualmente.

![image](../../imagens/vscode-languangemodes.png)

Note que o ícone exibido ao lado do nome do arquivo, no título da Aba, mudou, representando que estamos agora editando um arquivo de _Shell Script_. Você também vai notar que, à medida que você digita o script no conteúdo do arquivo, o vscode, que agora está informado de que estamos editando um arquivo no modo Shell Script, vai formatar o conteúdo de acordo com a sintaxe.

Podemos, também, abrir um dos scripts que já escrevemos na aula anterior. Para fazer isto, temos algumas opções:
- Voltar à aba com a página Welcome e clicar no link "Open File..."
- Clicar no menu File e selecionar a opção "Open File..."
- Usar as teclas de atalho _Ctrl+O_

Em qualquer uma destas formas, uma caixa de diálogo será exibida para que você possa selecionar o arquivo que deseja abrir. Selecione o arquivo `fancy.sh` (que criamos no final da última aula) para abrí-lo.

Note que o vscode já identificou o modo de linguagem do arquivo e selecionou "Shell Script". Normalmente o vscode tenta fazer isto automaticamente quando abrimos um arquivo, baseado na extensão do arquivo aberto. Ou quando salvamos o arquivo em disco (no caso de um arquivo novo), e finalmente atribuímos uma extensão quando lhe damos um nome. Normalmente, ele consegue determinar o modo de linguagem com sucesso. Eventualmente ele pode inferir o modo de linguagem para uma linguagem que ainda não é suportada, e pode sugerir que você procure uma extensão adequada para instalar o modo de linguagem apropriado.

!!! note
	Por padrão, o vscode suporta _JavaScript_, _TypeScript_, _HTML_, _CSS_, _SCSS_ e _JSON_, mas, como veremos adiante, é possível instalar suporte à inúmeras outras linguagens.
