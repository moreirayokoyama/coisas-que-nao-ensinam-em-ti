---
title: 🚧 4.7 - Trabalhando com Branches
---

## 🚧 4.7 - Trabalhando com Branches
Até aqui, você tem ouvido falarmos a respeito de uma _branch_ chamada _main_. E até aqui, nós tentamos não falar muito a respeito de nenhuma das duas coisas até que tivéssemos tratado os conceitos básicos por trás de um Controle de Versionamento de Código e do git.

Agora, uma vez visto as principais capacidades e usos da ferramenta, parece ser o momento ideal para conversarmos sobre _branches_, o que é a _main_ e como podemos usar outras branches na hora de trabalhar com git.

No nosso dia-a-dia trabalhando com código, existem situações específicas em que antecipamos a probabilidade de que a alteração que precisamos fazer, potencialmente, faça com que as coisas deixem de funcionar. Às vezes, entendemos que algumas mudanças estruturais sejam necessárias, ou simplesmente temos que fazer certas atualizações, e ainda não estamos seguros de que elas funcionarão bem com o restante do código, comprometendo a sua integridade.

Em casos assim, seria conveniente encontrarmos uma forma de trabalhar que não comprometesse a integridade do código e as alterações dos demais membros do time. Para isto, usamos _branches_.

Branches (_ramos_ em português), são uma forma de criarmos uma linha do tempo paralela ao histórico de alterações do repositório git. Algo parecido com a ideia de "Realidades Paralelas" seguindo a analogia de "Viagem no Tempo" que usamos até aqui.

Nós podemos iniciar uma branch na qual possamos trabalhar e fazer as alterações necessárias, sem correr o risco de que elas "quebrem" o código que está na _main_ e, no momento em que acharmos adequado, possamos finalmente "unir" as duas realidades novamente, integrando as alterações feitas (e devidamente testadas e estabilizadas) ao código principal, centralizando seus esforços.

Vamos ver como funciona.

### 4.7.1 - Criando e navegando por branches
O comando que iremos usar agora nos exibe uma lista de todas as branches presentes no nosso repositório.

```bash
git branch
```

Neste momento, somente a branch `main` está visível, por que é a única branch que existe. Para  criarmos uma nova branch, usamos o mesmo comando, usando como argumento o nome da branch que queremos criar.

```bash
git branch realidade-paralela
git branch
```

Agora temos duas branches. 

- git branch
- git switch
- git checkout
- git tag
