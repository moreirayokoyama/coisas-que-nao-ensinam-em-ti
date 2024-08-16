---
title: 4.4 - Usando o git para viajar no tempo
---
Voltemos ao cenário que estamos tentando simular: O arquivo README.md foi excluído em um commit, e descobrimos que isto foi um erro. Ele não deveria ter sido removido. Neste exato momento, o `git log` nos diz que o _HEAD_ está apontando para o commit que fez a alteração. Mover o _HEAD_ é a operação que nos permite caminhar pela linha do tempo e desfazer a história que o repositório conhece. Fazemos isso usando o comando `git reset`, passando como argumento o id do commit para o qual queremos voltar.

```bash
git reset e1c705034ed7eb64cf9305f360f36fe0ba94a0f6
git log
```

Observe o que o git log nos diz agora. O commit que removia o arquivo README.md desapareceu da história. E agora o _HEAD_ (junto com a branch  `main`) estão apontando para o commit inicial.

Mas se executarmos o comando `ls`, não vemos lá o arquivo README.md. O diretório continua vazio. Mas se você usar o comando `git status` vai reparar que existem mudanças prontas para serem registradas em um commit. E a mudança é justamente a exclusão do arquivo.

É como se o comando `git reset` tivesse nos enviado devolta exatamente para o momento anterior ao último commit que fizemos, quando a alteração já estava na área de staging. Tudo o que precisamos fazer agora, é cancelar o staging, e mudamos a história:

```bash
git restore README.md
```

E lá está o arquivo de volta, como se nunca tivesse sido excluído.

Mas e o commit que tínhamos feito? O que aconteceu com ele?

Ele ainda existe, e ainda está no banco de dados do repositório. E você poderia, se quisesse, usar novamente o comando `git reset` para fazer o _HEAD_ voltar a apontar para ele. Ou você poderia simplesmente ignorá-lo e voltar a trabalhar no seu diretório, reconstruindo a história a partir do ponto onde está agora.
