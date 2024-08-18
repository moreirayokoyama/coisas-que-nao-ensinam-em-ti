---
title: 🚧 4.7 - Trabalhando com Branches
---
Até aqui, você tem ouvido falarmos a respeito de uma _branch_ chamada _main_. E até aqui, nós tentamos não falar muito a respeito de nenhuma das duas coisas até que tivéssemos tratado os conceitos básicos por trás de um Controle de Versionamento de Código e do git.

Agora, uma vez visto as principais capacidades e usos da ferramenta, parece ser o momento ideal para conversarmos sobre _branches_, o que é a _main_ e como podemos usar outras branches na hora de trabalhar com git.

No nosso dia-a-dia trabalhando com código, existem situações específicas em que antecipamos a probabilidade de que a alteração que precisamos fazer, potencialmente, faça com que as coisas deixem de funcionar. Às vezes, entendemos que algumas mudanças estruturais sejam necessárias, ou simplesmente temos que fazer certas atualizações, e ainda não estamos seguros de que elas funcionarão bem com o restante do código, comprometendo a sua integridade.

Em casos assim, seria conveniente encontrarmos uma forma de trabalhar que não comprometesse a integridade do código e as alterações dos demais membros do time. Para isto, usamos _branches_.

Branches (_ramos_ em português), são uma forma de criarmos uma linha do tempo paralela ao histórico de alterações do repositório git. Algo parecido com a ideia de "Realidades Paralelas" seguindo a analogia de "Viagem no Tempo" que usamos até aqui.

Nós podemos iniciar uma branch na qual possamos trabalhar e fazer as alterações necessárias, sem correr o risco de que elas "quebrem" o código que está na _main_ e, no momento em que acharmos adequado, possamos finalmente "unir" as duas realidades novamente, integrando as alterações feitas (e devidamente testadas e estabilizadas) ao código principal, centralizando seus esforços.

Vamos ver como funciona.

## 4.7.1 - Criando e navegando por branches
O comando que iremos usar agora nos exibe uma lista de todas as branches presentes no nosso repositório.

```bash
git branch
```

Neste momento, somente a branch `main` está visível, por que é a única branch que existe. Para  criarmos uma nova branch, usamos o mesmo comando, usando como argumento o nome da branch que queremos criar.

```bash
git branch realidade-paralela
git branch
```

Agora é possível ver que temos duas branches no nosso repositório. A nova branch está disponível, mas o repositório ainda aponta para a branch `main`, como indicado com o asterisco.

Se executarmos o comando `git log`, teremos uma informação nova onde costumávamos conferir o commit para onde a _HEAD_ aponta, que costumava apresentar `HEAD -> main`, mas agora apresenta também, de forma complementar, o nome da branch que acabamos de criar: `HEAD -> main, realidade-paralela`.

Esta informação, exibida como parte da descrição do commit, é chamada, na documentação do git, de _ref names_. Isso está ligado ao conceito de _referências_, que é parte do modelo de dados de um repositório git, e que veremos com mais detalhes em breve. Neste momento, tudo o que sabemos a respeito disto, é que ele nos mostra o commit para onde a _HEAD_ aponta, e em que brach ele foi criado e quais outras branchs também estão apontando para ele (no caso, a branch que acabamos de criar).

Para mudarmos para a nova branch, podemos usar o comando `git switch`.

```bash
git switch realidade-paralela
git branch
```

O resultado do comando `git branch` demonstra que agora estamos na branch que acabamos de criar. Exceto pelo fato desta indicação, o processo da criação de uma nova branch não provoca nenhuma alteração na árvore de diretórios do repo. Todos os arquivos se encontram exatamente da mesma forma como quando estávamos na branch `main`.

Outra forma de conferir que estamos em uma branch diferente da `main` é através do comando `git status`. A primeira informação impressa por este comando indica a branch atual:

```
On branch realidade-paralela
```

Antes de começarmos a fazer mudança, vamos apenas entender exatamente o que mudou na prática. E para explicar isso, execute novamente o comando `git log`, e repare que _HEAD_, agora, aponta para a nova branch, e não mais para `main`.

## 4.7.2 - Fazendo commits na nova branch
Agora que criamos uma nova branch, podemos fazer modificações que afetem o estado dela, preservando o estado da `main`. Vamos criar algumas alterações no nosso projeto para ver isto funcionando. Crie um novo arquivo e salve em `./receitas/indice-de-receitas.md`, altere o `README.md` para incluir um link ao novo arquivo e faça um commit.

Veja agora como fica a situação do nosso repositório através do comando `git log`:
```
commit d01c4ea5fbf79f72800bf4d3f49695d557c1dd8d (HEAD -> realidade-paralela)
Author: Daniel Moreira Yokoyama <792153+moreirayokoyama@users.noreply.github.com>
Date:   Sat Aug 17 10:34:46 2024 -0300

    Criando o índice de receitas

commit 520c8cb0b182b3acb1dfd5348412eff63fde7cd3 (main)
Author: Daniel Moreira Yokoyama <792153+moreirayokoyama@users.noreply.github.com>
Date:   Tue Aug 13 14:56:12 2024 -0300

    Criando arquivo para sugestões de projeto

commit 014639823549e17df731dfb78eb859438f9eed4f
[...]
```

Note como as referências foram afetadas com o nosso novo commit. _HEAD_ agora avançou junto com a branch atual, deixando a `main` apontando para o commit anterior. Nós podemos avançar com a branch `realidade-paralela` por quantos commits acharmos necessários, a afastando cada vez mais de como as coisas estavam na `main` no momento em que ela foi criada.

## 4.7.3 - Criando linhas do tempo paralelas
Vamos imaginar um cenário hipotético em que, no meio das alterações que estamos fazendo na nossa branch `realidade-paralela`, nos demos conta de novas alterações necessárias no nosso repositório, que não estão relacionadas a esta branch, mas sim à `main`. Para realizar estas alterações, vamos precisar trocar novamente a branch atual, desta vez, de volta para a `main`.

```bash
git switch main
git log
```

Observe, conferindo a saída do comando `git log`, agora que voltamos para a branch `main`, que a branch `realidade-paralela` sumiu. Por padrão, o comando `git log` exibe apenas o histórico baseado no commit para o qual a _HEAD_ aponta. Se houverem referências que apontam para os commits exibidos neste histórico, elas serão exibidas. Mas a branch `realidade-parelala` está apontando para um commit que não tem mais relação com aquele para o qual a `main` aponta.

Se quisermos voltar a enxergar o histórico relacionado à branch `realidade-paralela`, basta usarmos o nome da branch como argumento ao comando `git log`.

```bash
git log realidade-paralela
```

De fato, a forma como temos usado `git log` até aqui é, basicamente, a mesma coisa que vemos quando executamos `git log HEAD`., que é o padrão para o comando, quando não informamos nenhuma referência como argumento.

Agora, vamos fazer a alteração necessária na `main`. Vamos supor que alguém fez uma recomendação de leitura, e queremos acrescentá-la a nossa lista de sugestões de estudo. Abra o arquivo de sugestões de estudo, acrescente um link para o livro "Pense Python" (https://penseallen.github.io/PensePython2e/) e faça um commit.

Agora que ambas as branches avançaram para além do commit que elas possuem em comum, o resultado do `git log` vai exibir somente o histórico de uma delas, já que ambas apontam para commits que não estão mais relacionados. Para conseguir enxergar ambas as branches na saída do comando, podemos usar como argumento o nome das duas.

```bash
git log main realidade-parelela
```

Importante observar que, independente de quais branches estivermos consultando o comando `git log`, os commits serão sempre exibidos na ordem cronológica, com o commit mais recente no topo, e o commit mais antigo no final da lista.

Outra forma de conseguir visualizar informações sobre todas as branches (e outras referências do nosso repositório) é através da opção `--all`.

```bash
git log --all
```

É razoável alertar que, à medida que o repositório começa a ter inúmeras referências (como diferentes branches, além de outros tipos que veremos em breve), a saída do comando `git log --all` pode se tornar pouco amigável.

Vamos tornar esse histórico um pouco mais interessante. Copie o código a seguir (ou fique à vontade se preferir digitá-lo manualmente), para criar alguns commits novos em ambas as branches:
```bash
echo "- Aplicação de Lista de Tarefas" >> ./projetos/sugestoes-de-projeto.md
git commit -am "Incluindo um novo projeto para Lista de Tarefas"
git switch realidade-paralela
mkdir musicas
echo "# Músicas para aprender a tocar" > ./musicas/indice-de-musicas.md
echo "- [Músicas para aprender a tocar](./musicas/indice-de-musicas.md)" >> README.md
git add .
git commit -m "Adicionando lista de músicas para aprender a tocar"
```

E agora, se executarmos o comando `git log --all`, podemos ter uma ideia de como os commits podem ser exibidos de forma confusa, e atrapalhar a nossa compreensão sobre como as linhas do tempo evoluíram, caso seja este o nosso interesse. Uma forma de melhorar esta visualização é usando a opção `--graph`, que exibe junto à saída uma representação do grafo das linhas do tempo junto aos commits.

```bash
git log --all --graph
```

Agora, conseguimos visualizar os commits de uma forma que seja possível rastrear as alterações na ordem em que elas foram feitas, de acordo com as branches onde foram feitas, e entender o históricos mesmo em branches diferentes.

Agora que sabemos avançar com o histórico de ambas as branches, como podemos fazer para, no momento oportuno, reunir ambas, trazendo as mudanças da realidade-paralela para se tornarem parte da história da `main`? É o que veremos a seguir.

