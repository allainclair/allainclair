# sync_calls.py
from asyncio import run, sleep
from random import uniform
from time import perf_counter


async def main() -> None:
	start = perf_counter()
	for i in range(5):
		print(await my_simulated_io_task(i + 1))
	end = perf_counter()
	print(f"All Tasks have been completed in {end - start:.3f} seconds.")


async def my_simulated_io_task(id_: int) -> str:
	wait_time = uniform(1, 5)
	await sleep(wait_time)
	return f"I/O Task {id_} has been completed after {wait_time:.3f} seconds."


if __name__ == "__main__":
	run(main())
