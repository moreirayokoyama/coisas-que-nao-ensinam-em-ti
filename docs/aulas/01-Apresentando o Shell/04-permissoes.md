---
title: 1.4 - Permissões de arquivos e diretórios
---
![image](../../imagens/permissoes-ls-l.png)

Eu mencionei que a primeira coluna exibida como resultado do `ls -l` são as permissões dos arquivos ou diretórios listados. Estas permissões indicam quem pode fazer o que com estes artefatos. Para dar uma breve  explicação, vamos entender como estas informações são exibidas:

Cada caractere exibido nesta coluna representa um atributo do artefato ao qual ele está ligado. O primeiro caractere, por exemplo, indica que tipo de artefato é o item da lista. Um simples `-` indica que ele é apenas um arquivo, e um `d` indica que ele é um diretório. Existem outros tipos, que podemos discutir no futuro.

Os demais caracteres são agrupamentos de 3 caracteres, cada caractere simbolizando uma permissão específica: `rwx`.
- `r`: representa a permissão para leitura
- `w`: representa a permissão para escrita
- `x`: representa a permissão para execução

Os 3 caracteres estão sempre nesta ordem, e podem ser substituídos por um `-`, indicando que a devida operação não é permitida.

Por exemplo:
`rwx`: Todas as operações são permitidas
`rw-`: É permitido ler e alterar o arquivo, mas não é permitido executá-lo
`r--`: Só se tem acesso para ler o conteúdo do arquivo, mas não é permitido alterá-lo.

Estas permissões são exibidas na seguinte ordem:
- Permissões para o dono do arquivo
- Permissões para os demais usuários do grupo dono do arquivo
- Permissões para todos os demais usuários

Por exemplo (retirado do screenshot acima):
`drwxr-xr-x  2 root root  4096 Mar 25  2022 X11`
Esta linha diz que `X11` é um diretório (`d`), o dono (que é o usuário `root`) possui permissão de leitura, escrita e execução, enquanto que os outros membros do grupo `root` podem apenas ler o conteúdo e executá-lo, bem como todos os outros usuários.

!!! important
	Em um **diretório**, a permissão de execução significa que o usuário é capaz de navegar por ele (através do comando `cd`). A permissão de leitura significa que o usuário é capaz de listar o conteúdo (através do comando `ls`) ou procurar por arquivos, etc. E a permissão de escrita significa que o usuário é capaz de criar novos artefatos (arquivos, diretórios, etc) dentro do diretório.
