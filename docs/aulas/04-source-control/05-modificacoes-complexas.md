---
title: 4.5 - Fazendo modificações mais complexas em arquivos e subdiretórios
---

Vamos começar a fazer algumas coisas um pouco mais complexas, como costuma ser o caso em projetos. Para isto, vamos criar alguns arquivos com resultados de comandos para simular um projeto em andamento. Na vida real, como você deve imaginar, as alterações no dia-a-dia de um projeto não são tão triviais, e iremos discutir isso um pouco olhando para projetos reais em breve. Então, tenha em mente que este exercício é só para nos ajudar a compreender cenários mais complexos.

Vamos criar um subdiretório chamado `estudos`, e nele um arquivo chamado `sugestoes-de-estudo.md`, e inserir alguns assuntos que temos interesse em estudar.
```Markdown
# Sugestões de Estudo

- [Python Funcional (Dunossauro)](https://dunossauro.github.io/python-funcional/)
- [FastAPI do Zero (Dunossauro)](https://fastapidozero.dunossauro.com/)
- [Curso básico de Bash (Blau Araújo)](https://www.youtube.com/watch?v=ZM--I3NJ2jY&list=PLXoSGejyuQGpf4X-NdGjvSlEFZhn2f2H7)
- [Além do Bash (Blau Araújo)](https://www.youtube.com/watch?v=_W51nj5JTwk&list=PLXoSGejyuQGpen1lAlhngkpuldmot8DV0)
```

Salve o arquivo e atualize o arquivo README.md com um link para a nova página.
```Markdown

- [Sugestões de estudo](./estudos/sugestoes-de-estudo.md)
```

Com as alterações feitas, vamos registrar um commit.
```bash
git add . # Adiciona todas as alterações feitas na árvore para o staging
git commit -m "Criando o arquivo para sugestões de estudo"
```

Observe as saída impressa pelo commit:
```
[main c39f63f] Criando página de sugestões de estudo
 2 files changed, 8 insertions(+)
 create mode 100644 estudos/sugestoes-de-estudo.md
```

Agora, vamos criar um outro subdiretório chamado `projetos`, e igualmente um arquivo chamado `sugestoes-de-projeto.md`, e inserir alguns projetos interessantes que podemos criar para treinar nossas habilidades.

```Markdown
# Sugestões de Projeto

- Blog Pessoal
	- MkDocs
	- Blog Plugin
- Aplicação de Organização Financeira
```

Da mesma forma, salve o arquivo, adicione um link no arquivo README.md e faça um commit.

Mais uma vez, observe a saída impressa pelo commit:
```
[main 95634d3] Criando página de sugestões de projeto
 2 files changed, 8 insertions(+), 1 deletion(-)
 create mode 100644 projetos/sugestoes-de-projeto.md
```

Vamos analisar o nosso histórico:

```bash
git log
```

Podemos ver os 3 commits no histórico e, como vimos anteriormente, o commit que fazia e exclusão do README.md de fato não faz mais parte da história.

O comando `git log` possui diversas opções que podemos usar para facilitar a visualização do histórico de commits. Por exemplo, nós podemos simplificar a visualização dos commits para serem exibidos em uma única linha contendo o id e o título da descrição usada na mensagem. Para isto, usamos a opção `--pretty=oneline`.

```bash
git log --pretty=oneline
```

A opção `pretty`, como já vimos, aceita `oneline` para simplificar os detalhes dos commits exibidos no histórico, e `raw` para dar uma versão mais detalhada de cada commit. Outras alternativas disponíveis definem o nível de detalhe desejado para a exibição: `short`, `medium` (esta é a opção usada por padrão, quando nenhuma outra é usada), `full` e `fuller` (além de outras).

Vamos agora ver com mais detalhes o segundo commit no nosso histórico.

```bash
git show c39f63fabb07933254661fe5c2f6ebb148069c97 --pretty=raw
```

Os detalhes que o comando `git show` nos mostra agora, detalha, como era de se esperar, todas as alterações feitas no diretório na ocasião do commit.

Não são apenas commits que o `git show` pode dar detalhes a respeito quando o usamos. De fato, nós podemos obter informações de quaisquer artefatos armazenados pelo banco de dados do repositório git. Por exemplo, os commits nos informam o id da Árvore para o qual apontam. Se usarmos o comando `git show` para dar informações sobre a árvore do nosso commit, passando o id da árvore como argumento, é isso que ele nos mostra:

```bash
git show 86b9b6c14632e0006fee09f44962541babc58b59
```
```
tree 86b9b6c14632e0006fee09f44962541babc58b59

README.md
estudos/
```

Ele mostra o conteúdo da árvore (no caso, o conteúdo dela no momento em que o commit foi criado). Outra forma útil de listar o conteúdo de uma árvore, é através do comando `git ls-tree`.

```bash
git ls-tree 86b9b6c14632e0006fee09f44962541babc58b59
```
```
100644 blob f974d4d88a6f072cddfeecb2a68ceaca16b7c75d    README.md
040000 tree 273fa08120ebbe98d52196b8635d78f5fb0eca7b    estudos
```

Observe que estamos consultando o repositório baseado num commit anterior, em que a situação do nosso diretório era diferente de como está agora. Podemos visualiar como estava o arquivo README.md no momento deste commit usando o comando `git cat-file` usando o id do blog como exibido pelo último comando:

```bash
git cat-file -p f974d4d88a6f072cddfeecb2a68ceaca16b7c75d
```

Note como nesta versão ainda não existia o link para as sugestões de projeto, que só foi adicionado posteriormente.
