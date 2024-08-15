---
title: Aula 04 - Sistema de Controle de Versionamento de Código - Git
description: Usando um Sistema de Controle de Versionamento de Código como ferramenta de viagem no tempo e colaboração em projetos com código
---

Trabalhar com código requer organização, e muito do que aprendemos sobre como organizamos o nosso código se dá com um trabalho iterativo e incremental, ou seja, o código está em constante mudança. Parte da nossa rotina no trabalho com código é de fazer, desfazer e refazer partes dele ao longo do desenvolvimento de uma tarefa, à medida que testamos e percebemos oportunidades de melhoria, ou até mesmo, problemas que não foram antecipados e que requerem mudanças na forma como havíamos elaborado a solução anteriormente.

Para ter algum controle sobre como estas alterações acontecem, e que possamos visualizá-las em um contexto histórico que torne essa organização possível, usamos um sistema de controle de versionamento de código. Existem diversas ferramentas para este fim disponíveis no mercado, mas uma delas se tornou um padrão de uso entre profissionais de TI nas últimas décadas: o Git.

O Git é um Sistema de Controle de Versionamento de Código (_SVC_), criado pelo Linus Torvalds enquanto ele desenvolvia o Kernel do Linux, disponível como software livre de código aberto sob a licença GPL, compatível com várias plataformas (Linux, MacOS e Windows). Ele é utilizado pela vasta maioria dos profissionais de tecnologia atualmente, tanto para projetos de Código Aberto quanto em organizações privadas.

Ele funciona através da criação de um repositório de código em um diretório no sistema de arquivos para acompanhar as mudanças que este código sofre ao longo do tempo. Neste repositório você é capaz de criar marcações do estado dos arquivos, e a partir destas marcações você tem a possibilidade de visualizar e navegar pelo histórico de como estes arquivos foram alterados, restaurar o estado em que eles se encontravam em um determinado momento no passado e reescrever a história deles a partir de uma marcação específica, além de diversas capacidades que veremos a seguir.

Nesta aula vamos explorar o uso de Git, tanto para organização pessoal, quanto para contribuição em projetos colaborativos.
