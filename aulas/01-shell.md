# Aula 1 - O _Shell_
Nesta primeira aula do nosso curso, apresentaremos o _Shell_ como uma ferramenta primária de produtividade das pessoas que trabalham em diversas áreas de TI.

Quando navegamos pela internet através do uso de um _Web Browser_, ou usamos algum _app_ ou qualquer aplicativo com uma interface gráfica, estamos limitados ao que esta interface suporta. Se existe um botão disponível para uma determinada funcionalidade, a visibilidade deste botão é o que determina se podemos nos beneficiar desta dela ou não. Se o botão não está visível, não podemos clicar nele.

Uma interface de linha de comando (_CLI_), como a que temos quando usamos um _Shell_, torna mais flexível o acesso que temos às funcionalidades disponíveis.

Saber usar o _Shell_ e navegar por ele potencialmente torna o trabalho cotidiano mais produtivo e, por isto, estamos dando o devido foco em apresentá-lo neste curso.

## 1. O que é o _Shell_
Quase todas as plataformas com as quais você pode trabalhar atualmente oferecem um _Shell_, e muitas oferecem diferentes opções de _Shell_ para você escolher. Apesar de que eles possam variar em seus detalhes, em sua essência são basicamente iguais: eles te permitem executar programas, manipular sua entrada (_input_) e inspecionar sua saída (_output_) de uma forma semi-estruturada.

### 1.1 _Shell_ vs _Terminal_
Para ter acesso a um Shell, você precisa de um _Terminal_. Um terminal é um programa capaz de receber um comando, encaminhar para o _Shell_, e exibir seu resultado.

O sistema que você usa em seu computador provavelmente possui um terminal disponível. Para os usuários de Windows (a partir do Windows 11), têm instalado em seu sistema o _Windows Terminal_. Para usuários de versões anteriores, o _Windows Terminal_ está disponível para download gratuito na Microsoft Store. Outras opções de terminal para os usuários Windows são o _ConEmu_ e o _Cmder_.

Já para os usuários de Linux/MacOS, existem diversas opções de terminal. Um dos terminais mais famosos para os usuários MacOS é o _iTerm2_. No Linux, entre os terminais mais usados estão o _Terminator_ e o _Guake_.

Escolher entre as diferentes opções de terminais normalmente depende das funcionalidades e conveniências que cada opção oferece. Painéis (_tiles_), Guias(_tabs_), Teclas de Atalho, Esquemas de Cores, e outras facilidades podem diferenciar as opções de terminais, mas de uma forma ou de outra, a maioria dos terminais disponíveis oferecem estas e outras funcionalides com algumas diferenças sutis de como elas funcionam.

### 1.2 Diferentes Shells
Além dos diferentes sabores de terminais, existem também diferentes opções de Shells. Cada Shell pode apresentar uma sintaxe diferente de comandos e da forma como você interage através do terminal, apesar de haver muitas semelhanças entre as principais opções.

Para os usuários Windows, as duas principais opções de Shell disponíveis são:

- _cmd_

O _cmd_ é o shell nativo do Windows, baseado no _Prompt de Comando_ do antigo _MS-DOS_ (sistema operacional da Microsoft anterior ao Windows). Ele suporta basicamente os comandos básicos do MS-DOS para navegar e manipular o sistema de arquivos.

- _Windows PowerShell_

O _PowerShell_ é um Shell moderno criado pela Microsoft, como uma alternativa mais poderosa que o _cmd_ para os usuários Windows.

No mundo Linux e MacOS, existem opções similares de Shell, dentre elas as mais comuns são:

- _Bash_

O _Bash_ (_Bourne Again Shell_) é uma opção de Shell disponível para Linux e MacOS baseado no _Bourne Shell_, que é um Shell popular para o sistema _Unix_.

- _Zsh_

O _Zsh_ (z-shell) é uma alternativa ao Bash que apresenta funcionalidades comuns, e acrescenta outras funcionalidades baseadas em outras famosas opções de Shell do sistema _Unix_ (como o _ksh_ e o _tcsh_), além de trazer funcionalidades únicas.

## 2. Bash (Bourne Again SHell)
_Bash_ é o shell mais popular atualmente, sendo a opção pré-instalada no Ubuntu, que é a distribuição do Linux mais baixada, além é claro de fazer parte de outras distribuições também. Por causa da sua relevância, toda a discussão relacioana a Shells ao longo deste curso, quando não abordada de uma forma generalista, usará como premissa o uso do _bash_.

Para acompanhar o conteúdo deste curso, certifique-se de ter instalado o _bash_ como uma das opções de Shell disponíveis no seus sistema. Usuários Linux e MacOS provavelmente já possuirão o bash instalado, caso contrário, provavelmente encontrarão uma fácil instalação a partir de algum dos gerenciadores de pacote que seus sistemas disponibilizam.

### 2.1 Bash para Usuários Windows

Para aqueles que acompanham este curso e são usuários do Microsoft Windows, existem opções de instalação do Bash. Vamos apresentar 3 delas para que você escolher a que melhor lhe for mais conveniente.

- MinGW64 / Cygwin

Das opções disponíveis para se instalar o Bash no Windows, o MinGW64 e o Cygwin se diferenciam por não precisar virtualizar um outro sistema (como Linux). Ambos os projetos podem ser instalados em qualquer versão do Windows e fornecem um conjunto de ferramentas para criar um ambiente compatível com um sistema semelhante ao Unix para pessoas que preferem trabalhar usando o Windows.

O Bash disponibilizado por estas ferramentas, não é totalmente compatível com o Bash que você usaria ao criar uma instalação do Ubuntu, por exemplo, mas pode ser o suficiente para quem prefere não virtualizar (ou não pode).

Para instalar o MinGW64, acesse o site: https://www.mingw-w64.org/downloads/

**IMPORTANTE: Se você instalar o Git para Windows (haverão aulas neste curso que usarão o Git), ele inclui o MinGW64 para disponibilizar um shell chamado Git Bash.**

Se você preferir instalar o Cygwin, o endereço no site para baixar o instalador é: https://cygwin.com/install.html

- Criar um Memory Stick Inicializável com uma distribuição do Linux

É possível ter uma distribuição do Linux disponível para uso sem precisar instalá-la no seu sistema, usando um Memory Stick (vulgo: Pen Drive) inicializável.

Existem diversos tutoriais na disponíveis na internet explicando com realizar o processo. Mas, resumidamente, você precisa baixar a imagem do sistema operacional (por exemplo, Ubuntu), e um programa capaz de configurar um Memory Stick com a imagem de forma inicializável.

**IMPORTANTE: Esta opção torna necessário que você reincie o seu computador, e durante o uso do sistema escolhido, você não terá acesso aos recursos do Windows.**

- Dual Boot com Linux

Você pode criar uma instalação do Linux lado a lado com a instalação do Windows e ter a opção no seu dispositivo de qual dos sistemas você pretende usar no momento da inicialização.

**IMPORTANTE: Esta opção torna necessário que você reincie o seu computador, e durante o uso do sistema escolhido, você não terá acesso aos recursos do Windows.**

**IMPORTANTE 2: Este método exige que alguns recursos (por exemplo, espaço em disco) se tornem exclusivos para o novo sistema, tornando-os indisponíveis para o Windows. Isto requer algum planejamento sobre como estes recursos serão distribuídos.**

- Virtualização de Linux

Criar uma Máquina Virtual (_VM_) com uma instalação do Linux é uma opção acessível e, certamente, mais conveniente que a opção com Dual Boot. Uma VM é, basicamente, um computador virtual, com as mesmas funcionalidades que um dispositivo oferece, porém, emulado a partir de um Sistema Hospedeiro (no caso, o Windows).

Você pode criar VMs usando softwares gratuitos como o HyperV do Windows ou  [VirtualBox da Oracle](https://www.virtualbox.org/), e baixar uma imagem da distribuição Linux desejada (por exemplo, Ubuntu), para criar uma VM. Independente de qual plataforma você pretende usar, você vai precisar ativar o Hypervisor do Windows (que é parte integrante da instalação do HyperV). Para isto, no menu iniciar (pressionando a tecla Windows no teclado), digite "Ativar ou Desativar Recursos do Windows", e ao abrir a janela dos Recursos do Windows, procure na lista o ítem "Hyper-V" e certifique-se de que ele esteja selecionado. **Ativar este recurso, irá exigir que você reinicialize seu computador**.

**IMPORTANTE: Este método exige que alguns recursos (por exemplo, espaço em disco) sejam compartilhados com a VM, podendo ter um impacto na performance do sistema hospedeiro.**

- Windows Subsystem for Linux (WSL)

Para usuários de versões mais recentes do Windows (a partir do Windows 10), é possível virtualizar uma distribuição Linux usando um Kernel disponível pelo próprios Windows. Este é, inclusive, o método que eu estou usando. É um método melhor do que criar uma VM, pois o WSL suporta uma integração transparente entre os sistemas (compartilhando portas e programas).

Este método também exige que você ative o _HyperV_, além de ativar também o "Subsistema do Windows para Linux", e instalar a distribuição escolhida (por exemplo, Ubuntu), a partir das opções disponíveis na Microsoft Store.

### 2.2 Navegando com o Shell
- `pwd`
- `cd`
- Caminhos (path)
    - Caminho absoluto (`/`)
    - Caminho Relativo
        - `~`, `.`, `..`, `-`
- `ls`
### 2.3 Manipulação do sistema de arquivos
- `mkdir`
- `touch`
- `cp`
- `mv`
- `rm`
### 2.4 Programas Básicos
- `echo`
- `cat`
- `find`
### 2.5 Conectando Programas
- Standard Input/Output
- Redirecionamento de Streams
    - Output (`>`)
    - Append (`>>`)
    - Input (`<`)
    - Pipe (`|`)
### 2.6 Outros Programas úteis
- `tee`
- `grep`
- `tail`
- `head`
- `less`

