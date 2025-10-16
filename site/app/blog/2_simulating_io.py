# simulating_io.py
from asyncio import run, sleep
from random import uniform


async def main() -> None:
	print(await my_simulated_io_task(1))


async def my_simulated_io_task(id_: int) -> str:
	wait_time = uniform(1, 5)
	await sleep(wait_time)
	return f"I/O Task {id_} has been completed after {wait_time:.3f} seconds."


if __name__ == "__main__":
	run(main())
