---
title: Aula 05 - Usando a interface de linha de comando (CLI)
description: Padrões e conveniências no uso de ferramentas que usamos na interface de linha de comando.
---
# Aula 05 - A Interface de Linha de Comando

## 2.7 Pseudo-dispositivos úteis
Pseudo dispositivos são dispositivos falsos que podemos usar para alguns fins específicos durante o uso do terminal, como usá-los como stream de entrada ou de saída na execução de programas.

### 2.7.1 `/dev/null`
O primeiro pseudo-dispositivo que iremos ver é o `/dev/null`, para o qual todos os bytes escritos são descartados. É uma forma de religar o stream de saída e/ou o stream de erro para serem ignorados quando não nos importamos com eles.

```bash
ls -lha /bin > /dev/null
```

A instrução acima executa o comando `ls` no diretório `/bin` mas religa o stream de saída ao pseudo-dispositivo `/dev/null` fazendo com que a saída seja completamente ignorada, e somente mensagens de erro serão escritas no terminal.