## [Domine Async IO em Python: Exemplos Práticos que Melhoram Performance](/blog/mastering-async-io-in-python)

### Resumo

**Resumindo:** vamos ver como escrever código [Async IO](https://docs.python.org/3/library/asyncio.html)
em Python com exemplos, focados em reduzir o tempo de execução e fornecer alternativas de código.
Vamos começar do simples e depois ir para o mais complexo.

**Links rápidos para as seções:** [Hello World!](#hello-world) | [Simulando IO com sleep()](#simulando-io-com-sleep)
| [Chamadas síncronas com funções Async IO](#chamadas-síncronas-com-funções-async-io)
| [Chamadas assíncronas com funções Async IO usando gather()](#chamadas-assíncronas-com-funções-async-io-usando-gather)
| [Chamadas assíncronas com resultados que precisam ser modificados](#chamadas-assíncronas-com-resultados-que-precisam-ser-modificados)
| [Chamadas assíncronas com funções Async IO usando TaskGroup](#chamadas-assíncronas-com-funções-async-io-usando-taskgroup)
| [TaskGroup com vinculação de variável](#taskgroup-com-vinculação-de-variável)
| [Considerações](#considerações)

Async IO é uma forma de executar muitas tarefas de I/O concorrentemente (chamadas de rede, consultas a banco de dados,
leituras/escritas de arquivos) sem bloquear o programa. Isso não cria múltiplas threads;
ele roda em um **único loop de eventos** que gerencia quando as tarefas são pausadas e resumidas.

Este conteúdo não está vinculado apenas ao Python, mas os exemplos serão em Python.
Presumo que as funcionalidades de Async IO do Python estejam disponíveis em outras linguagens que suportam Async IO.

Qualquer problema, sugestão, comentário ou correção, **entre em contato comigo.**

### Hello World!

Esta é a forma como definimos uma função async e como executá-la:
<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F1_hello_world.py%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>
<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F1_hello_world_output.txt%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>


### Simulando IO com sleep()

O código a seguir simula IO usando `random.uniform` para aguardar de 1 a 5 segundos e imprimir a saída de `my_simulated_io_task`.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F2_simulating_io.py%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>
<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F2_simulating_io_output.txt%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

### Chamadas síncronas com funções Async IO

Vamos começar com o seguinte código que tem chamadas síncronas usando funções async IO; você deve evitar chamadas síncronas se possível.
Muitas vezes, vejo algo similar a isto, e eu refatoro para ter chamadas assíncronas.
Se as funções `async são independentes, você deve chamá-las assincronamente na maioria dos casos. Vou mostrar isso nas próximas
seções, mas veja a seção [Considerações](#considerações) para entender porque em alguns casos devemos usar chamadas síncronas.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F3_sync_calls.py%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

Note que `my_simulated_io_task` está definida como `async, mas o loop for das linhas 9 e 10 chama a função
sincronamente; a Task 2 deve aguardar a Task 1 ser completada, e assim por diante.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F3_sync_calls_output.txt%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

Note que a ordem das tarefas é mantida (Task 1, 2, 3, ...). Levou mais de 17 segundos para finalizar. É a soma de todos os tempos das tarefas.

### Chamadas assíncronas com funções Async IO usando [gather()](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather)

Agora vamos melhorar a performance destas tarefas. O código a seguir chama as funções assincronamente.
Também estamos adicionando alguns `prints` para ver essas tarefas rodando.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F4_async_gather.py%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>
<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F4_async_gather_output.txt%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

Note que os resultados são mantidos em ordem após a chamada de [`gather()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather),
mas as tarefas podem finalizar em uma ordem diferente devido ao tempo de execução de cada função.
Todas as tarefas foram completadas **em 4.426 segundos porque as tarefas foram executadas assincronamente**. Está muito próximo da Task 3,
a tarefa mais lenta, 4.424 segundos. Você pode ganhar performance significativa executando tarefas de I/O usando Async IO.
Veja a seção [Considerações](#considerações) para ver casos onde você deve estar atento.

### Chamadas assíncronas com resultados que precisam ser modificados

Há casos onde você precisa modificar os resultados das chamadas assíncronas. Neste caso, estou mostrando um exemplo
onde quero apenas os resultados das tarefas que têm índices pares, mas poderia ser qualquer outra coisa.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F5_gather_even.py%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

Note que precisei adicionar uma instrução `if` na linha 15 para imprimir apenas tarefas com índices pares.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F5_gather_even_output.txt%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

Isso funciona bem. Note novamente que a ordem dos resultados é mantida (Task 2, 4). Agora vamos resolver tudo no
primeiro loop `for` como mostrado na próxima seção.

### Chamadas assíncronas com funções Async IO usando TaskGroup

Você pode ver em `async_gather.py` e `gather_even.py` que você vai receber os resultados das
funções async apenas na chamada `await gather`, e no `gather_even.py`, você precisa usar uma instrução `if`
para filtrar os resultados das tarefas ímpares. Podemos mudar `gather_even.py` para resolver tudo no primeiro `for`
usando [TaskGroup](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup) no código a seguir:

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F6_task_group.py%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

`add_done_callback` executa após cada tarefa ser completada e o resultado da tarefa será impresso para índices pares (linha 14).

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F6_task_group_output.txt%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

Note que os resultados das tarefas são impressos em uma ordem diferente! Neste caso, a tarefa mais rápida (Task 4) é impressa primeiro, e assim por diante.

Esta abordagem é válida para evitar iterar sobre os resultados novamente para resolver algo que você precisa.
Se você conhecia apenas o `gather` e o usou muitas vezes, você pode ver que o `TaskGroup` pode ser uma alternativa
ao `gather` em alguns casos porque você pode evitar loops extras para trabalhar o resultado da tarefa.

### TaskGroup com vinculação de variável

Um exemplo final para mostrar como modificar os resultados no *callback* de cada tarefa. Queremos vincular uma 'coisa'
(`my_thing`) aleatória a cada tarefa e imprimi-la com os resultados no loop for da linha 23.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F7_task_group_with_results.py%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

`thing=my_thing` da linha 19 vincula o valor atual do loop `for` de `my_thing` à função lambda. Isso ajuda a trabalhar com
este valor logo após a tarefa ser completada.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F7_task_group_with_results_output.txt&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

### Considerações

- Lançar muitas tarefas assincronamente pode "inundar" serviços, e você pode começar a ter mensagens do tipo "muitas requisições" para suas chamadas assíncronas.
  Para superar isso, envie requisições em lotes (*batch*), ou até sincronamente se o tempo de execução não for um grande problema.

- Tenha cuidado com exceções que podem acontecer dentro das tarefas. Dependendo do que você está resolvendo, você deve lidar com essas exceções.

- As linhas 17-19 de `task_group_with_results.py` mostram que você precisa adicionar um parâmetro lambda para evitar usar a
  última `my_thing` para todos os callbacks. Este parâmetro garantirá que você vincule a `my_thing` atual de cada iteração.
