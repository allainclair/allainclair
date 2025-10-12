# hello_world.py
from asyncio import run


async def main() -> None:
	print("Hello, world!")


if __name__ == "__main__":
	run(main())
