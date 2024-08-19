---
title: 🚧 4.8 - Unificando o Histórico de Branches com Merge
---
Trabalhar com branches enquanto fazemos experimentações, ou enquanto as alterações necessárias quebram o funcionamento do projeto, ou qualquer que seja a razão para usá-las, eventualmente nos leva a um ponto em que queremos integrar as alterações à `main`. Quando chegamos a este ponto, é o momento de usarmos o comando `git merge`.

O `git merge` recebe como argumento uma branch, de onde gostaríamos de obter todas as alterações e aplicá-las à branch atual.

O que acontece quando executamos este comando é:
- O git busca estabelecer qual é o _commit_ mais recente em comum com as duas branches.
- A partir deste commit, o git levanta o histórico de todos os commits realizados na branch de origem
- Um _diff_ é calculado com as alterações feitas por estes commits
- Um novo commit é criado na branch de destino aplicando as alterações obtidas pelo _diff_
- Finalmente, o git solicita uma mensagem que, após ser devidamente preenchida e salva, será aplicada ao novo commit que fará parte do histórico da branch de destino.

Vamos ver o `git merge` em ação:

```bash
git switch main # certifique-se de que estamos na `main`
git merge realidade-paralela
```

O git irá abrir o editor esperando uma mensagem descrevendo o novo commit. Após salvar a mensagem e fechar o editor, o commit é realizado.

Abra o seu editor e navegue pelos arquivos do diretório para ver as alterações aplicadas. Note como o arquivo README.md se encontra, além da presença dos diretórios `receitas` e `musicas`, que foram incorporados da branch `realidade-paralela` para a `main`, onde estamos agora.

Vamos ver o resultado do commit, consultando o log das alterações:
```bash
git log --graph
```

Podemos ver um novo commit aplicado à branch `main`, incorporando as alterações feitas até o commit mais recente na branch `realidade-paralela`. Vamos olhar este commit com mais atenção:

```bash
git show HEAD --pretty=raw
```

```
commit a768ed465b2c06816d56bcb968b8f79ad7f73412
tree bf91313be494c799e8757b6e8da30b97db36abd7
parent a9022c9092815862911895b488ad8e2461ebb507
parent 09d7b98baf5ec29a887daaecd8a604ce35a00e5a
author Daniel Moreira Yokoyama <792153+moreirayokoyama@users.noreply.github.com> 1724073862 -0300
committer Daniel Moreira Yokoyama <792153+moreirayokoyama@users.noreply.github.com> 1724073862 -0300

    Merge branch 'realidade-paralela'

(END)
```

Preste atenção na peculiaridade deste commit. Ele possui dois `parents`. Isto basicamente o distingue como um _commit de merge_.

Observe que a branch `realidade-paralela` ainda existe, e não foi afetada pela operação. Ela continua sem ter incorporadas as alterações feitas na `main`. Mas, digamos que nós estejamos interessados em continuar fazendo alterações nela e, pra fazer isto, seria conveniente atualizá-la também.

```bash
git switch realidade-paralela
git merge main
git log --all --graph
```

Note que, desta vez, o git não solicitou uma mensagem para o merge. E o resultado no git log mostra que o merge que fizemos anteriormente é para onde a branch `realidade-paralela` está apontando agora. Isto é o resultado de uma operação chamada "Fast-forward", que é quando o git identifica que as alterações feitas no merge podem ser simplificadas, já que o histórico de commits da branch que está sendo incorporada já resolve as alterações de forma incremental.

Como o commit mais recente na main era um merge cujo um dos parents era é o commit mais recente até então na branch `realidade-paralela`, o git é capaz de entender que as alterações feitas já foram aplicadas e só o oque ele faz é atualizar a referência da branch para o commit de merge.

Com isto, neste momento, conseguimos ter uma ideia básica de como o `git merge` funciona. Mas precisamos, agora, nos aprofundar em cenários mais complexos e, ainda assim, corriqueiros no dia-a-dia quando trabalhamos usando o git.





- git merge
- Conflitos
