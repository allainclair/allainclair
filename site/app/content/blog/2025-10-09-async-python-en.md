## [Mastering Async IO in Python: Practical Examples That Boost Performance](/blog/mastering-async-io-in-python)

### Summary

**In short:** we are going to see how to write [Async IO](https://docs.python.org/3/library/asyncio.html) 
code in Python with examples, focused on reducing running time and providing code alternatives.
Let's start from the simple and then go more complex.

**Quick links for sections:** [Hello World!](#hello-world) | [Simulating IO with sleep()](#simulating-io-with-sleep)
| [Sync calls with Async IO functions](#sync-calls-with-async-io-functions)
| [Async calls with Async IO functions using gather()](#async-calls-with-async-io-functions-using-gather)
| [Async calls with results that need to be modified](#async-calls-with-results-that-need-to-be-modified)
| [Async calls with Async IO functions using TaskGroup](#async-calls-with-async-io-functions-using-taskgroup)
| [TaskGroup with variable binding](#taskgroup-with-variable-binding)
| [Considerations](#considerations)

Async IO is a way to run many I/O-bound tasks concurrently (network calls, database queries,
file reads/writes) without blocking the program. This doesn't create multiple threads;
it runs on a **single event loop** that manages when tasks are paused and resumed.

This content is not only bound to Python, but the examples will be in Python.
I presume that Async IO features from Python are available in other languages that support Async IO.

Any issue, suggestion, comment, or correction, **please contact me.**

### Hello World!

This is how we define an async function and how to run it:
<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F1_hello_world.py%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>
<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F1_hello_world_output.txt%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>


### Simulating IO with sleep()

The following code simulates IO using `random.uniform` to wait from 1 to 5 seconds and print the output of `my_simulated_io_task`.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F2_simulating_io.py%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>
<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F2_simulating_io_output.txt%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

### Sync calls with Async IO functions

Let's start with the following code that has sync calls using async IO functions; you should avoid sync calls if possible.
Many times, I see something similar to this, and I refactor it to have async calls.
If the async functions are independent, you should call them asynchronously in most cases. I will show this in the next
sections, but see the [Considerations](#considerations) section to understand why in some cases we should use sync calls.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F3_sync_calls.py%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

Note that `my_simulated_io_task` is defined as async, but the for loop of lines 9 and 10 calls the function
synchronously; task 2 must wait for task 1 to be completed, and so on.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F3_sync_calls_output.txt%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

None that the task order is kept (task 1, 2, 3, ...). It took more than 17 seconds to finish it. It is the sum of all the tasks' times.

### Async calls with Async IO functions using [gather()](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather)

Now we are going to improve the performance of these tasks. The following code calls the functions asynchronously.
We are also adding some prints to see these tasks running.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F4_async_gather.py%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>
<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F4_async_gather_output.txt%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

Note that the results are kept in order after the [`gather()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather) 
call, but the tasks can finish in a different order due to the running time of each function.
All tasks were completed **in 4.426 seconds because the tasks were run asynchronously**. It is very close to the task 3,
the slowest task, 4.424 seconds. You can gain significant performance by running IO-bound tasks using Async IO.
See the [Considerations](#considerations) section to see cases where you should be aware of.

### Async calls with results that need to be modified

There are cases where you need to modify the results of the async calls. In this case, I am showing an example
where I want only the results of the tasks that have even indexes, but it could be anything else.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F5_gather_even.py%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

Note that I needed to add an `if` statement at line 15 to print only tasks with even indexes.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F5_gather_even_output.txt%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

This works fine. Note again that the order of the results is kept (Task 2, 4). Now we will resolve everything in the
first `for` loop as shown in the next section.

### Async calls with Async IO functions using TaskGroup

You can see in the `async_gather.py` and `gather_even.py` that you are going to receive the results of the
async functions only in the `await gather` call, and in the `gather_even.py`, you need to use an `if` statement
to filter out the odd tasks' results. We can change `gather_even.py` to resolve everything in the first `for`
using [TaskGroup](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup) in the following code:

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F6_task_group.py%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

`add_done_callback` runs after each task is completed and the task result will be printed for even indexes (line 14).

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F6_task_group_output.txt%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

Note that the task results are printed in a different order! In this case, the shorter task (Task 4) is printed first, and so on.

This approach is valid to avoid iterating over the results again to solve something that you need.
If you only knew `gather` and you used it many times, you can see that `TaskGroup` can be an alternative
to `gather` in some cases because you can avoid extra loops to work the task's result.

### TaskGroup with variable binding

A final example to show how to modify the results in the callback of each task. We want to bind a random 'thing'
to each task and print it with the results in the for loop of line 23.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F7_task_group_with_results.py%3Fts%3D4&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

`thing=my_thing` of line 19 binds the current `for` loop value of `my_thing` to the lambda function. It helps to work with
this value right after the task is completed.

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Fallainclair%2Fallainclair%2Fblob%2Fmaster%2Fsite%2Fapp%2Fblog%2F7_task_group_with_results_output.txt&style=github-dark&type=code&showLineNumbers=on&showFullPath=on&showCopy=on"></script>

### Considerations

- Launching many tasks asynchronously could "flood" services, and you can start having "too many requests" kind of messages for your async calls.
  To overcome this, send requests in batches, or even synchronously if running time is not a big issue.

- Take care of exceptions that can happen inside the tasks. Depending on what you are solving, you must handle these exceptions.

- Lines 17-19 of `task_group_with_results.py` show that you need to add a lambda parameter to avoid using the
  last `my_thing` for all the callbacks. This parameter will guarantee that you bind the current `my_thing` of each iteration.
