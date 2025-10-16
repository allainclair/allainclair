# task_group.py
from asyncio import run, sleep, TaskGroup
from random import uniform
from time import perf_counter


async def main() -> None:
	start = perf_counter()
	async with TaskGroup() as tg:
		for i in range(5):
			tg.create_task(my_simulated_io_task(i + 1)).add_done_callback(
				lambda task, i=i + 1: i % 2 == 0 and print(task.result())
			)

	end = perf_counter()
	print(f"All Tasks have been completed in {end - start:.3f} seconds.")


async def my_simulated_io_task(id_: int) -> str:
	wait_time = uniform(1, 5)
	print(f"I/O Task {id_} has started, waiting for {wait_time:.3f} seconds...")
	await sleep(wait_time)
	return f"I/O Task {id_} has been completed after {wait_time:.3f} seconds."


if __name__ == "__main__":
	run(main())
