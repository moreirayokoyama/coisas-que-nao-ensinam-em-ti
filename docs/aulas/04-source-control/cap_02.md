---
title: 4.2 - Iniciando um Repositório
---

Vamos agora entender como começamos a trabalhar com Git. O primeiro conceito que precisamos aprender sobre Git é o Repositório (informalmente chamado de _repo_). Sempre que você quiser trabalhar com o Git, você vai precisar criar um repositório. Um repositório é, de certa forma, um repositório no seu sistema de arquivos. Isto é conveniente, já que normalmente nós colocamos usamos diretórios como forma de organizar nossos projetos, então é natural que pensemos que, toda vez que criamos um diretório para trabalhar em um projeto, este mesmo diretório é um candidato em potencial para se tornar o repositório Git daquele projeto.

Se você já tem um projeto em andamento ou se vai começar um do zero, não importa, para criar um repo você só precisa entrar na pasta e iniciar o repositório:

```bash
mkdir novo_projeto && cd novo_projeto
git init
```

Uma mensagem será exibida dizendo que um repositório iniciado no diretório `.git` dentro do diretório do projeto. Como vimos na [aula de shell](../01-shell/index.md), diretórios e arquivos cujo nome começam com `.`, não são exibidos por padrão quando listamos o conteúdo do diretório. Para visualizar o diretório criado, podemos usar o `ls --all` (ou `ls -a`).

Exceto pela presença deste subdiretório, a criação repo parece não ter tido efeito nenhum no diretório do projeto em si. E é assim mesmo que um repositório funciona. Ele não interfere na forma como você interage com seus arquivos e subdiretórios de projeto. O único indício real de que estamos em um repositório git é a presença do subdiretório `.git`.

Não é recomendável que você altere manualmente o conteúdo de qualquer um dos artefatos dentro do diretório `.git`. Este subdiretório deve ser usado somente pelo próprio git. O conteúdo deste subdiretório é o banco de dados que o git irá usar pra fazer o acompanhamento das mudanças que você faz no seu projeto. Qualquer modificação feita manualente nestes dados pode comprometer a confiabilidade da ferramenta.

Mais adiante falaremos sobre como esse banco de dados funciona, mas por hora vamos compreender como trabalhamos com o repositório que temos em mãos.

### 4.2.1 - Primeiras Interações com o Repositório.
A forma mais básica de interação com um repositório é através do comando `git status`, que nos trás informações de qual a sua situação atual. Como acabamos de criá-lo, o comando nos mostrará as seguintes informações:

```
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

Basicamente o que ele diz é:
- Em que branch estamos: `main` (falaremos sobre branches mais adiante)
- Não existem commits ainda (falaremos sobre commits a seguir)
- Não há nada pronto para criar um commit
	- Crie ou copie arquivos e use `git add` para acompanhar

!!! Importante

	Se você tiver criado um repositório em um diretório que já possuia arquivos, a mensagem exibida será diferente por este motivo, mencionando de que existem arquivos ainda não acompanhados pelo git.

Vamos criar um arquivo para ver como o git reage com as modificações que fazemos no nosso repositório.

```bash
touch teste.txt
git status
```

Note como a mensagem exibida está diferente agora. Ela nos avisa de que existe um arquivo no diretório que não está sendo acompanhado pelo git (_Untracked files_). Se removermos este arquivo, e, mais uma vez, consultarmos o status do repositório, observamos que a mensagem exibida é identica a que tivemos anteriormente.

```bash
rm teste.txt
git status
```

O git consegue reconhecer quando existem diferenças entre o conhecimento que ele tem do repositório e a situação atual do diretório, e se baseia na comparação entre ambos para te informar a respeito do status. Ou seja, quando você desfaz as alterações, o git entende que repositório está em sincronia com a situação do diretório.

### 4.2.2 - Adicionando Arquivos ao Repositório
Vamos criar um arquivo para incluirmos no repositório. Em repositórios git, é muito comum criar-se um arquivo descritivo chamado README.md. A extensão `md` indica que o arquivo está no formato _Markdown_, que é um arquivo de texto redigido usando marcações simples para formatar o seu conteúdo, como criar títulos, subtítulos, links, listas formatadas, etc.

```bash
touch README.md
git status
```

Agora, vamos entender melhor o que o git está tentando nos dizer quando exibe esta mensagem sobre arquivos não acompanhados.

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
		README.md

nothing added to commit but untracked files present (use "git add" to track)
```

A mensagem diz: use "git add <arquivo>..." para incluir no commit. Para incluir arquivos ao nosso repositório, precisamos entender como o git gerencia o estado do repositório primeiro.

Nós começamos a criar alterações no repositório através de uma operação chamada _commit_. Commit, em português, significa "comprometer" em uma tradução literal, mas o que queremos dizer é que estamos efetuando um _registro_ das alterações que estamos fazendo.

Na prática, porém, um commit é análogo a uma "fotografia" da situação do repositório em um determinado momento. O processo de criar um commit é, seguindo a analogia, o processo de criar uma composição da fotografia que queremos registrar.

Nós montamos esta composição através de uma etapa intermediária chamada "staging". À medida que entendemos que o diretórios está pronto pra ter seu estado registrado em um commit, nós podemos montar este commit, colocando as alterações que fizemos nesta estapa intermediária, através do comando `git add`.

```bash
git add README.md
git status
```

Observe a saída do comando `git status` agora:
```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
		new file:   README.md
```

Neste momento, o git nos informa que o arquivo README.md (que está indicado como um novo arquivo), está entre as mudanças que estão prontas para serem registradas em um commit (_Changes to be committed_). Nesta situação, o git entende que o arquivo README.md faz parte do repositório e, portanto, precisa ser acompanhado (_tracked_) a partir de agora.

A mensagem também nos mostra como podemos, se quisermos, remover o README.md do _staging_. Isto faria com que o arquivo voltasse à situação anterior, ou seja, voltasse a ser um arquivo desconhecido (_untracked_) para o repositório.

```bash
git rm --cached README.md
git status
```

Isto, como descrito na mensagem impressa, colocou o arquivo README.md na mesma situação que ele se encontrava anteriormente. O que faz certo sentido, visto que o arquivo ainda se encontra vazio. Vamos colocar algum conteúdo nele para criarmos nosso primeiro commit.

```markdown
# Novo Projeto
Este repositório foi criado para explorar a ferramenta git sendo usada num projeto.
```

Assumindo que este seja o estado ideal do arquivo README.md para termos um primeiro registro no histórico do nosso repositório, vamos finalmente criar nosso primeiro commit. Para isto, precisaremos novamente adicioná-lo à etapa de _staging_.

```bash
git add README.md
```

Na analogia da fotografia, a etapa de _staging_ se compara à forma como posicionamos as coisas antes de fotofrafá-las. A área de staging é a forma como podemos "montar" o commit que desejamos criar. Isso nos dá a flexibilidade de manter outras alterações pendentes fora do commit que estamos montando.

O próximo passo é, finalmente, criarmos o commit, registrando a criação do arquivo README.md no nosso repositório.

```bash
git commit
```

No momento em que executamos este comando, um editor de textos será aberto (de acordo com a configuração que fizemos, será o vscode) com um arquivo chamado *COMMIT_EDITMSG* para digitarmos uma descrição do commit que estamos criando. O comando no shell não será finalizado até que salvemos uma mensagem e fechemos o editor do arquivo.

É uma boa prática fazermos uma mensagem descritiva sobre as alterações feitas no repositório registradas em um commit. E isto, normalmente, é um acordo feito entre as pessoas que contribuem com o projeto.

Existem times que adotam a um modelo de mensagem, contendo uma estrutura acordada sobre como a descrição deve ser feita. Isto é muito frequente em projetos de código aberto mantidos por uma comunidade, a ponto de ser comum haver, no repositório, um arquivo contendo as diretrizes que os contribuidores do projeto precisam seguir para criar novos commits.

Além disso, existem também convenções criadas ao redor de certas práticas nas mensagens dos commits, como [_Conventional Commits_](https://www.conventionalcommits.org/), criado para ter automações que serão executadas baseadas nas mensagens dos commits, e [GitMoji](https://gitmoji.dev/), uma convenção de Emojis que podem ser usados para serem associados com tipos específicos de alterações registradas no commit, que ajudam a ter uma comunicação visual mais eficiente a respeito do mesmo.

Para os fins deste tutorial, podemos usar uma mensagem simples, como:

```
Criação do arquivo README.md, descrevendo projeto.
```

Salve e feche o editor deste arquivo, para ver o comando ser concluído no shell. Uma mensagem confirmando o commit é exibida, mostrando a descrição que demos ao commit e um relatório resumido do seu conteúdo.

Note que ele exibe algumas informações interessantes:
- `[main (root-commit) e1c7050]`:
	- `main`: indica que este commit foi feito na branch `main`
	- `root-commit`: indica que este é o commit raiz do repositório.
	- `e1c7050`: Esta sequência de caracteres é uma versão curta do identificador do commit, como veremos a seguir.
- `1 file changed, 0 insertions(+), 0 deletions(-)`: Este é um relatório resumido das alterações que este commit fez ao repositório
	- `1 file changed`: O primeiro valor deste relatório diz respeito a alterações feitas envolvendo um arquivo como um todo (como a criação de um arquivo, ou a remoção dele). No caso, ele contou a criação do arquivo README.md
	- `0 insertions(+), 0 deletions(-)`: Aqui o relatório se refere a inserções e deleções dentro de arquivos, e nós veremos como isso funciona em breve.

Se executarmos o comando `git status` novamente, teremos uma mensagem diferente.

```bash
git status
```
```
On branch main
nothing to commit, working tree clean
```

A mensagem `No commits yet` não é mais exibida, pois agora existe um commit no nosso repositório. Além disso, ele também diz que não há nenhuma mudança atual no diretório. O arquivo README.md está devidamente registrado.

Uma forma de conferirmos o commit que acabamos de criar é através do comando `git log`. Ele produz uma lista do histórico de commits em nosso repositório, que por ora, possui apenas um commit, o que acabamos de fazer.

```bash
git log
```
```
commit e1c705034ed7eb64cf9305f360f36fe0ba94a0f6 (HEAD -> main)
Author: Daniel Moreira Yokoyama <792153+moreirayokoyama@users.noreply.github.com>
Date:   Sat Aug 10 10:58:38 2024 -0300
	Criação do arquivo README.md, descrevendo projeto.
```

Aqui podemos ver algumas informações já conhecidas a respeito do commit que acabamos de fazer, além de algumas outras informações novas. O identificador do commit, que vimos na forma curta logo após o commit ter sido feito, agora aparece na sua forma completa. Temos também os metadados conhecidos para o commit: o autor (com o seu nome e mail conforme configurmos anteriormente nesta aula), a data e hora em que ele foi criado e a descrição dada a ele.

Mas existe também esta informação nova: `(HEAD -> main)`. Você já sabe que `main` é o nome da branch atual (embora, talvez, você já esteja se perguntando sobre o que é uma branch há algum tempo), mas o que é `HEAD`?

Vamos conversar um pouco sobre como o git faz o acompanhamento (_tracking_) do estado do repositório, aprendendo um pouco sobre seu modelo de dados e seu funcionamento.
