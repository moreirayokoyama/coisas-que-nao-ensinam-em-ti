---
title: 2.7 - Shell Script
---

A capacidade de usar comandos de forma produtiva no Bash nos habilita a elevar esta produtividade através de scripts.

Scripts são arquivos contendo comandos que serão executados pelo shell em sequência, podendo servir como uma ferramenta de automação, ou até mesmo programação.

O uso de scripts usando Bash para automação é tão comum que existem profissionais em posições que se apoiam em Shell Script, como principal atividade no seu dia-a-dia.

Para criar um script, tudo o que precisamos fazer é criar um arquivo texto contendo a lista de comandos que queremos executar (convencionalmente, usando a extensão `.sh`) e o executamos religando o stream de entrada do comando `bash` ao arquivo do script.

!!! important
	O comando `bash` é, na realidade, o executável do shell que temos usado até agora. Ao invocarmos o comando `bash` passando o nosso script como argumento, não estamos fazendo nada diferente do que seria abrir o shell e executarmos os comandos manualmente. A única dirença é que estamos fazendo de forma automatizada.

Vamos ver como isto funciona.

### 2.7.1 - Criando e Executando Scripts
Vamos criar o nosso primeiro Script executando o famoso rito de iniciação que discutimos no início desta aula, `Olá, mundo`.

```bash
cat > ola.sh
echo "Olá, mundo"
```

Para executar nosso script, usamos o comando `sh`.
```bash
bash < ./ola.sh
```

O comando `sh` lê o conteúdo do arquivo `olá.sh` e o interpreta, executando seus comandos. Podemos, incrementar este script com mais comandos:

```bash
cat >> ola.sh
date
echo "Bom trabalho"
bash < ./ola.sh
```

Note como, desta vez, ele executou todos os comandos do nosso script.

Na verdade, o comando `bash` é capaz de receber um arquivo de script como argumento e interpretá-lo sem que precisemos religar seu stream de entrada.

```bash
bash ./ola.sh
```

Outra forma de executarmos um script, é transformando-o em um executável. Para isto, precisamos forncecer privilégios de execução para o usuário que pretende fazer este uso. Fazemos isto através do comando `chmod`

```bash
stat ./ola.sh
```
![image](../../imagens/stats.png)

!!! note
	O comando `stat` imprime o _status_ do arquivo no sistema. Informações úteis, como tamanho, permissões, data de criação, data da última modificação, quem é o _owner_ e outras.

Note, a sessão de acesso (_access_), que ele não possui permissões de execução para nenhum usuário (`-rw-r--r--`). Para conceder permissão de execução para o arquivo `ola.sh`, nós usamos o comando `chmod`. A permissão para execução é representada pelo caractere `x`.

```bash
chmod +x ola.sh
```

Agora, podemos conferir as permissões novamente através do comando `stat`.

```bash
stat ola.sh
```
![image](../../imagens/stats_executable.png)

Finalmente, com a devida permissão, somos capazes de executar o script.

```bash
./ola.sh
```

!!! note
	O motivo de precisarmos usar o endereço do nosso escript para executá-lo (`./`) é que, no _bash_ (bem como em diversos shells compatíveis com o _Unix_), o shell somente procura por executáveis que estão nos diretórios presentes n variável $PATH. O shell não procura por executáveis no diretório atual, como faz, por exemplo, o shell `cmd` do Windows.

	Portanto, no _Bash_ (e em outros shells compatíveis com unix, como o _dash_ ou o _zsh_), devemos apontar onde está o executável que pretendemos rodar, mesmo que ele esteja no diretório atual do shell, passando o caminho completo ou relativo do mesmo.

Mas, antes de prosseguirmos, vamos seguir a convenção de orientar ao shell sobre qual interpretador deverá usar ao executar nosso script, usando a notação chamada de _shebang_. O _shebang_ é a sequência dos caracteres `#!`, usada para sistemas compatíveis com _Unix_ (como o linux) para apontar ao shell qual é o interpretador do executável. No nosso caso, até aqui, estamos usando o próprio _bash_ como interpretador (`/bin/bash`), e será ele mesmo que usaremos no nosso _shebang_, mas este processo é importante, pois outros interpretadores estão disponíveis.

Então, precisamos colocar o `shebang` na primeira linha do arquivo e, para isto, precisamos editá-lo, e faremos isto usando o editor `vi`. Você pode usar outro editor de sua preferência. Falaremos de `Vim` e do `vscode` em aulas futuras. Para usuários Windows que não possuem interesse em usar o `vi`, é possível usar o _Bloco de Notas_. Basta executar o `notepad.exe`, passando como argumento o nome do arquivo.

```bash
vi ola.sh
```

O `vi` é um editor de textos _modal_ básico, disponível no _bash_. Modal significa que ele funciona em diferentes modos. No momento em que o abrimos, ele está no _modo de comando_ (command mode). Para editá-lo, precisamos alternar para o _modo de digitação_ (type mode).

Existem diferentes formas para alternarmos para o modo de digitação, mas a que iremos usar aqui aplica um comando antes: O comando shift+O cria uma linha acima da linha onde estamos posicionados (que é a primeira linha), e posiciona o cursor na nova linha em branco, mudando para o modo de digitação.

![image](../../imagens/vi-typemode.png)
Agora podemos digitar a nossa linha do _shebang_:
```bash
#!/bin/bash
```

Para concluir a edição, precisamos antes voltar para o modo de comando, usando a tecla ESC. De volta ao modo de comando, usamos o `:w` para salvar o arquivo (pressionando ENTER/RETURN logo em seguida). Para sair do editor _vi_, usamos o comando `:q` e pressionamos ENTER/RETURN.

Isto não afeta em nada o funcionamento do nosso script atual. Mas à medida que você aprende a viver no shell, você poderá criar outros tipos de script. Como, por exemplo, scripts em _Python_, que você poderá transformar em executáveis e usar um _shebang_ adequado para que o shell saiba como executá-los.

O exemplo a seguir pode não funcionar no seu sistema se você não possuir o interpretador do Python instalado.

```bash
which python
cat > ola.py
#!/usr/bin/python
print("Olá, mundo")
^C
chmod +x ola.py
./ola.py
```

Agora que vimos como podemos executar nossos scripts, vamos aprender como fazer melhor uso deles.

### 2.7.2 - Recebendo argumentos em Scripts
Ao longo destas aulas temos usado diversos comandos que recebem argumentos como forma de ter algum controle sobre o seu comportamento, e não é diferente com os scripts que podemos construir. O Bash nos permite receber argumentos em nossos scripts através de parâmetros numerados.

Para ler estes parâmetros, podemos usar variáveis especiais usando a notação com o sinal `$` e o número dos parâmetros de 1 a 9. Por exemplo:

!!! warning
	Não se esqueça de dar permissão de execução para os arquivos de script antes de testá-los

```bash
cat > params.sh
echo "Início da execução"
echo $1
echo "Fim da execução"
```

Uma variação do famoso "Olá, mundo", mas que consegue saudar uma pessoa:
```bash
cat > saudar.sh
echo "Olá, " $1
```

Um script de exemplo pra fazer um cálculo aritmético:
```bash
cat > soma.sh
echo $(($1 + $2))
```

Existem, também, outros parâmetros especiais para tornar o script mais dinâmico:
- `$@`: lista todos os parâmetros, não limitados a 9.
- `$#`: retorna o número de argumentos usados na execução do script
- `$0`: retorna o nome do script que está sendo executado
- `$$`: retorna o número do processo que executa o script
- `$?`: retorna o código de saída do programa anterior

```bash
cat > fancy.sh
echo "Iniciando a execução de $0 no processo $$"
echo "Usando $# parâmetros: $@"
ls -lha
echo "Resultado do comando: $?"
```
