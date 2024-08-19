---
title: 4.6 - Conferindo as alterações feitas no repositório entre commits
---
É muito comum, quando trabalhamos com projetos em código, ficarmos na dúvida sobre como as alterações no código o fizeram chegar ao estado atual, e o git nos dá ferramentas para acompanhar este histórico. O comando `git diff` pode ser usado de diversas formas pra dar detalhes nas alterações feitas ao longo do tempo no nosso repositório. Vamos experimentar algumas delas.

```bash
git diff c39f63fabb07933254661fe5c2f6ebb148069c97 95634d3efb106e86514d2e4eebdc5ba69e995a0d
```

```diff
diff --git a/README.md b/README.md
index f974d4d..e369b33 100644
--- a/README.md
+++ b/README.md
@@ -1,4 +1,5 @@
 # Novo Projeto
 Este repositório foi criado para explorar a ferramenta git sendo usada num projeto.

 - [Sugestões de estudo](./estudos/sugestoes-de-estudo.md)

+- [Sugestões de projeto](./projetos/sugestoes-de-projeto.md)
diff --git a/projetos/sugestoes-de-projeto.md b/projetos/sugestoes-de-projeto.md
new file mode 100644
index 0000000..cf70b9a
--- /dev/null
+++ b/projetos/sugestoes-de-projeto.md
@@ -0,0 +1,6 @@
+# Sugestões de Projeto
+
+- Blog Pessoal
+    - MkDocs
+    - Blog Plugin
+- Aplicação de Organização Financeira
```

Desta forma, o `git diff` exibe todas as alterações feitas de um commit para o outro. Podemos, por exemplo, fazer uma comparação mais abrangente, envolvendo o nosso primeiro commit e o commit mais recente.

```bash
git diff bda3c91a8280d30ceda53f23717ce4ce68be87ff 95634d3efb106e86514d2e4eebdc5ba69e995a0d
```

```diff
diff --git a/README.md b/README.md
index 5726bb6..e369b33 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,5 @@
 # Novo Projeto
 Este repositório foi criado para explorar a ferramenta git sendo usada num projeto.
+
+- [Sugestões de estudo](./estudos/sugestoes-de-estudo.md)
+- [Sugestões de projeto](./projetos/sugestoes-de-projeto.md)
diff --git a/estudos/sugestoes-de-estudo.md b/estudos/sugestoes-de-estudo.md
new file mode 100644
index 0000000..c27c06b
--- /dev/null
+++ b/estudos/sugestoes-de-estudo.md
@@ -0,0 +1,6 @@
+# Sugestões de Estudo
+
+- [Python Funcional (Dunossauro)](https://dunossauro.github.io/python-funcional/)
+- [FastAPI do Zero (Dunossauro)](https://fastapidozero.dunossauro.com/)
+- [Curso básico de Bash (Blau Araújo)](https://www.youtube.com/watch?v=ZM--I3NJ2jY&list=PLXoSGejyuQGpf4X-NdGjvSlEFZhn2f2H7)
+- [Além do Bash (Blau Araújo)](https://www.youtube.com/watch?v=_W51nj5JTwk&list=PLXoSGejyuQGpen1lAlhngkpuldmot8DV0)
diff --git a/projetos/sugestoes-de-projeto.md b/projetos/sugestoes-de-projeto.md
new file mode 100644
index 0000000..cf70b9a
--- /dev/null
+++ b/projetos/sugestoes-de-projeto.md
@@ -0,0 +1,6 @@
+# Sugestões de Projeto
+
+- Blog Pessoal
+    - MkDocs
+    - Blog Plugin
+- Aplicação de Organização Financeira
```

Podemos, inclusive, fazer uma comparação retroativa, usando como referência o commit mais recente, comparando-o com um commit anterior.

```bash
git diff 95634d3efb106e86514d2e4eebdc5ba69e995a0d bda3c91a8280d30ceda53f23717ce4ce68be87ff
```

```diff
diff --git a/README.md b/README.md
index e369b33..5726bb6 100644
--- a/README.md
+++ b/README.md
@@ -1,5 +1,2 @@
 # Novo Projeto
 Este repositório foi criado para explorar a ferramenta git sendo usada num projeto.
-
-- [Sugestões de estudo](./estudos/sugestoes-de-estudo.md)
-- [Sugestões de projeto](./projetos/sugestoes-de-projeto.md)
diff --git a/estudos/sugestoes-de-estudo.md b/estudos/sugestoes-de-estudo.md
deleted file mode 100644
index c27c06b..0000000
--- a/estudos/sugestoes-de-estudo.md
+++ /dev/null
@@ -1,6 +0,0 @@
-# Sugestões de Estudo
-
-- [Python Funcional (Dunossauro)](https://dunossauro.github.io/python-funcional/)
-- [FastAPI do Zero (Dunossauro)](https://fastapidozero.dunossauro.com/)
-- [Curso básico de Bash (Blau Araújo)](https://www.youtube.com/watch?v=ZM--I3NJ2jY&list=PLXoSGejyuQGpf4X-NdGjvSlEFZhn2f2H7)
-- [Além do Bash (Blau Araújo)](https://www.youtube.com/watch?v=_W51nj5JTwk&list=PLXoSGejyuQGpen1lAlhngkpuldmot8DV0)
diff --git a/projetos/sugestoes-de-projeto.md b/projetos/sugestoes-de-projeto.md
deleted file mode 100644
index cf70b9a..0000000
--- a/projetos/sugestoes-de-projeto.md
+++ /dev/null
@@ -1,6 +0,0 @@
-# Sugestões de Projeto
-
-- Blog Pessoal
-    - MkDocs
-    - Blog Plugin
-- Aplicação de Organização Financeira
```

Note como, neste momento, ele trata as alterações que, anteriormente, eram inclusões para, agora, remoções.

É possível, também, reduzir o escopo do comando `git diff` para exibir somente as alterações feitas num blob específico, ou em uma sub-árvore específica.

```bash
git diff bda3c91a8280d30ceda53f23717ce4ce68be87ff 95634d3efb106e86514d2e4eebdc5ba69e995a0d -- README.md
```

```diff
diff --git a/README.md b/README.md
index 5726bb6..e369b33 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,5 @@
 # Novo Projeto
 Este repositório foi criado para explorar a ferramenta git sendo usada num projeto.
+
+- [Sugestões de estudo](./estudos/sugestoes-de-estudo.md)
+- [Sugestões de projeto](./projetos/sugestoes-de-projeto.md)
```

Você pode obter o mesmo resultado usando o `git diff` comparando os ids que o blob possui nas árvores relacionadas a cada commit.
