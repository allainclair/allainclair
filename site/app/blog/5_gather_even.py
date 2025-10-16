# gather_even.py
from asyncio import run, sleep, gather
from random import uniform
from time import perf_counter


async def main() -> None:
	start = perf_counter()
	tasks = []
	for i in range(5):
		tasks.append(my_simulated_io_task(i + 1))

	results = await gather(*tasks)
	for i, result in enumerate(results, start=1):
		if i % 2 == 0:
			print(result)
	end = perf_counter()
	print(f"All Tasks have been completed in {end - start:.3f} seconds.")


async def my_simulated_io_task(id_: int) -> str:
	wait_time = uniform(1, 5)
	print(f"I/O Task {id_} has started, waiting for {wait_time:.3f} seconds...")
	await sleep(wait_time)
	return f"I/O Task {id_} has been completed after {wait_time:.3f} seconds."


if __name__ == "__main__":
	run(main())
