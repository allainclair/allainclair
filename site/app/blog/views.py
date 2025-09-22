from fasthtml import APIRouter
from fasthtml.common import Div, H2, Span, Figure, Img, H3, Pre, Code, A, Button, Br
from starlette.requests import Request
from datetime import datetime, UTC
from app.icons import language
from timeago import format

router = APIRouter()

CODE_STR_COLOR = "text-success"
CODE_KEYWORD_COLOR = "text-warning"
CODE_BUILT_IN_COLOR = "text-primary"
CODE_BASE_COLOR = "text-base-content"
CODE_FUNCTION_COLOR = "text-accent"
CODE_BASE_COLOR_50 = "text-base-content/50"

def code_1():
	return Div(
		Pre(
			Code(
				Span("# hello_world.py", cls=CODE_BASE_COLOR_50)
			),
			data_prefix="1"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("asyncio", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("run", cls=CODE_BASE_COLOR)
			), 
			data_prefix="2"
		),
		Pre(Code(""), data_prefix="3"),
		Pre(Code(""), data_prefix="4"),
		Pre(
			Code(
				Span("async", cls=CODE_KEYWORD_COLOR), " ",
				Span("def", cls=CODE_KEYWORD_COLOR), " ",
				Span("main", cls=CODE_FUNCTION_COLOR), "()", " -> ",
				Span("None", cls=CODE_KEYWORD_COLOR), ":"
			),
			data_prefix="5"
		),
		Pre(
			Code(
				"	",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(",
				Span('"Hello, world!"', cls=CODE_STR_COLOR), ")"
			),
			data_prefix="6"
		),
		Pre(Code(""), data_prefix="7"),
		Pre(Code(""), data_prefix="8"),
		Pre(
			Code(
				Span("if", cls=CODE_KEYWORD_COLOR), " ",
				Span("__name__", cls=CODE_BASE_COLOR), " == ",
				Span("\"__main__\"", cls=CODE_STR_COLOR), ":",
			),
			data_prefix="9"
		),
		Pre(
			Code(
				"	",
				Span("run(", cls=CODE_BASE_COLOR),
				Span("main())", cls=CODE_BASE_COLOR),
			),
			data_prefix="10"
		),
		cls="mockup-code w-full"
	)


def terminal_1():
	return Div(
		Pre(Code("python hello_world.py"), data_prefix="$", cls=CODE_BASE_COLOR),
		Pre(Code("Hello, world!"), data_prefix=">", cls=CODE_STR_COLOR),
		cls="mockup-code w-full"
	)


def code_2():
	return Div(
		Pre(
			Code(
				Span("# simulating_io.py", cls=CODE_BASE_COLOR_50)
			),
			data_prefix="1"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("asyncio", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("run", cls=CODE_BASE_COLOR), ", ",
				Span("sleep", cls=CODE_BASE_COLOR)
			), 
			data_prefix="2"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("random", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("uniform", cls=CODE_BASE_COLOR)
			), 
			data_prefix="3"
		),
		Pre(Code(""), data_prefix="4"),
		Pre(Code(""), data_prefix="5"),
		Pre(
			Code(
				Span("async", cls=CODE_KEYWORD_COLOR), " ",
				Span("def", cls=CODE_KEYWORD_COLOR), " ",
				Span("main", cls=CODE_FUNCTION_COLOR), "() -> ",
				Span("None", cls=CODE_KEYWORD_COLOR), ":"
			),
			data_prefix="6"
		),
		Pre(
			Code(
				"	",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(",
				Span("await", cls=CODE_KEYWORD_COLOR), " ",
				Span("my_simulated_io_task", cls=CODE_BASE_COLOR), "(1))"
			),
			data_prefix="7"
		),
		Pre(Code(""), data_prefix="8"),
		Pre(Code(""), data_prefix="9"),
		Pre(
			Code(
				Span("async", cls=CODE_KEYWORD_COLOR), " ",
				Span("def", cls=CODE_KEYWORD_COLOR), " ",
				Span("my_simulated_io_task", cls=CODE_FUNCTION_COLOR), "(id_: ",
				Span("int", cls=CODE_KEYWORD_COLOR), ") -> ",
				Span("str", cls=CODE_KEYWORD_COLOR), ":"
			),
			data_prefix="10"
		),
		Pre(
			Code(
				"	wait_time = ",
				Span("uniform", cls=CODE_FUNCTION_COLOR), "(1, 5)"
			),
			data_prefix="11"
		),
		Pre(
			Code(
				"	",
				Span("await", cls=CODE_KEYWORD_COLOR), " ",
				Span("sleep", cls=CODE_FUNCTION_COLOR), "(wait_time)"
			),
			data_prefix="12"
		),
		Pre(
			Code(
				"	",
				Span("return", cls=CODE_KEYWORD_COLOR), " ",
				Span("f\"I/O task {id_} completed after {wait_time:.3f} seconds.\"", cls=CODE_STR_COLOR)
			),
			data_prefix="13"
		),
		Pre(Code(""), data_prefix="14"),
		Pre(Code(""), data_prefix="15"),
		Pre(
			Code(
				Span("if", cls=CODE_KEYWORD_COLOR), " ",
				Span("__name__", cls=CODE_BASE_COLOR), " == ",
				Span("\"__main__\"", cls=CODE_STR_COLOR), ":"
			),
			data_prefix="16"
		),
		Pre(
			Code(
				"	",
				Span("run(", cls=CODE_BASE_COLOR),
				Span("main())", cls=CODE_BASE_COLOR)
			),
			data_prefix="17"
		),
		cls="mockup-code w-full"
	)


def terminal_2():
	return Div(
		Pre(Code("python simulating_io.py"), data_prefix="$", cls=CODE_BASE_COLOR),
		Pre(Code("I/O task 1 completed after 4.713 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		cls="mockup-code w-full"
	)


def code_3():
	return Div(
		Pre(
			Code(
				Span("# sync_calls.py", cls=CODE_BASE_COLOR_50)
			),
			data_prefix="1"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("asyncio", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("run", cls=CODE_BASE_COLOR), ", ",
				Span("sleep", cls=CODE_BASE_COLOR)
			), 
			data_prefix="2"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("random", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("uniform", cls=CODE_BASE_COLOR)
			), 
			data_prefix="3"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("time", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("perf_counter", cls=CODE_BASE_COLOR)
			), 
			data_prefix="4"
		),
		Pre(Code(""), data_prefix="5"),
		Pre(Code(""), data_prefix="6"),
		Pre(
			Code(
				Span("async", cls=CODE_KEYWORD_COLOR), " ",
				Span("def", cls=CODE_KEYWORD_COLOR), " ",
				Span("main", cls=CODE_FUNCTION_COLOR), "() -> ",
				Span("None", cls=CODE_KEYWORD_COLOR), ":"
			),
			data_prefix="7"
		),
		Pre(
			Code(
				"	start = ",
				Span("perf_counter", cls=CODE_BASE_COLOR), "()"
			),
			data_prefix="8"
		),
		Pre(
			Code(
				"	",
				Span("for", cls=CODE_KEYWORD_COLOR), " i ",
				Span("in", cls=CODE_KEYWORD_COLOR), " ",
				Span("range", cls=CODE_BUILT_IN_COLOR), "(10):"
			),
			data_prefix="9"
		),
		Pre(
			Code(
				"		",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(",
				Span("await", cls=CODE_KEYWORD_COLOR), " ",
				Span("my_simulated_io_task", cls=CODE_BASE_COLOR), "(i+1))"
			),
			data_prefix="10"
		),
		Pre(
			Code(
				"	end = ",
				Span("perf_counter", cls=CODE_BASE_COLOR), "()"
			),
			data_prefix="11"
		),
		Pre(
			Code(
				"	",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(",
				Span("f\"All tasks completed in {end - start:.3f} seconds.\"", cls=CODE_STR_COLOR), ")"
			),
			data_prefix="12"
		),
		Pre(Code(""), data_prefix="13"),
		Pre(Code(""), data_prefix="14"),
		Pre(
			Code(
				Span("async", cls=CODE_KEYWORD_COLOR), " ",
				Span("def", cls=CODE_KEYWORD_COLOR), " ",
				Span("my_simulated_io_task", cls=CODE_FUNCTION_COLOR), "(id_: ",
				Span("int", cls=CODE_KEYWORD_COLOR), ") -> ",
				Span("str", cls=CODE_KEYWORD_COLOR), ":"
			),
			data_prefix="15"
		),
		Pre(
			Code(
				"	wait_time = ",
				Span("uniform", cls=CODE_FUNCTION_COLOR), "(1, 5)"
			),
			data_prefix="16"
		),
		Pre(
			Code(
				"	",
				Span("await", cls=CODE_KEYWORD_COLOR), " ",
				Span("sleep", cls=CODE_FUNCTION_COLOR), "(wait_time)"
			),
			data_prefix="17"
		),
		Pre(
			Code(
				"	",
				Span("return", cls=CODE_KEYWORD_COLOR), " ",
				Span("f\"I/O task {id_} completed after {wait_time:.3f} seconds.\"", cls=CODE_STR_COLOR)
			),
			data_prefix="18"
		),
		Pre(Code(""), data_prefix="19"),
		Pre(Code(""), data_prefix="20"),
		Pre(
			Code(
				Span("if", cls=CODE_KEYWORD_COLOR), " ",
				Span("__name__", cls=CODE_BASE_COLOR), " == ",
				Span("\"__main__\"", cls=CODE_STR_COLOR), ":"
			),
			data_prefix="21"
		),
		Pre(
			Code(
				"	",
				Span("run(", cls=CODE_BASE_COLOR),
				Span("main())", cls=CODE_BASE_COLOR)
			),
			data_prefix="22"
		),
		cls="mockup-code w-full"
	)


def terminal_3():
	return Div(
		Pre(Code("python sync_calls.py"), data_prefix="$", cls=CODE_BASE_COLOR),
		Pre(Code("I/O task 1 completed after 4.712 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 2 completed after 4.988 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 3 completed after 2.790 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 4 completed after 2.320 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 5 completed after 1.929 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 6 completed after 2.639 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 7 completed after 4.105 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 8 completed after 1.422 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 9 completed after 3.453 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 10 completed after 1.907 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("All tasks completed in 30.278 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		cls="mockup-code w-full"
	)


def code_4():
	return Div(
		Pre(
			Code(
				Span("# async_gather.py", cls=CODE_BASE_COLOR_50)
			),
			data_prefix="1"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("asyncio", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("run", cls=CODE_BASE_COLOR), ", ",
				Span("sleep", cls=CODE_BASE_COLOR), ", ",
				Span("gather", cls=CODE_BASE_COLOR)
			), 
			data_prefix="2"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("random", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("uniform", cls=CODE_BASE_COLOR)
			), 
			data_prefix="3"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("time", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("perf_counter", cls=CODE_BASE_COLOR)
			), 
			data_prefix="4"
		),
		Pre(Code(""), data_prefix="5"),
		Pre(Code(""), data_prefix="6"),
		Pre(
			Code(
				Span("async", cls=CODE_KEYWORD_COLOR), " ",
				Span("def", cls=CODE_KEYWORD_COLOR), " ",
				Span("main", cls=CODE_FUNCTION_COLOR), "() -> ",
				Span("None", cls=CODE_KEYWORD_COLOR), ":"
			),
			data_prefix="7"
		),
		Pre(
			Code(
				"	",
				"start = ",
				Span("perf_counter", cls=CODE_BASE_COLOR), "()"
			),
			data_prefix="8"
		),
		Pre(
			Code(
				"	",
				"tasks = []"
			),
			data_prefix="9"
		),
		Pre(
			Code(
				"	",
				Span("for", cls=CODE_KEYWORD_COLOR), " i ",
				Span("in", cls=CODE_KEYWORD_COLOR), " ",
				Span("range", cls=CODE_BUILT_IN_COLOR), "(10):"
			),
			data_prefix="10"
		),
		Pre(
			Code(
				"		",
				"tasks.append(",
				Span("my_simulated_io_task", cls=CODE_BASE_COLOR), "(i+1))"
			),
			data_prefix="11"
		),
		Pre(Code(""), data_prefix="12"),
		Pre(
			Code(
				"	",
				"results = ",
				Span("await", cls=CODE_KEYWORD_COLOR), " ",
				Span("gather", cls=CODE_FUNCTION_COLOR), "(*tasks)"
			),
			data_prefix="13"
		),
		Pre(
			Code(
				"	",
				Span("for", cls=CODE_KEYWORD_COLOR), " result ",
				Span("in", cls=CODE_KEYWORD_COLOR), " results:"
			),
			data_prefix="14"
		),
		Pre(
			Code(
				"		",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(result)"
			),
			data_prefix="15"
		),
		Pre(
			Code(
				"	end = ",
				Span("perf_counter", cls=CODE_BASE_COLOR), "()"
			),
			data_prefix="16"
		),
		Pre(
			Code(
				"	",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(",
				Span("f\"All tasks completed in {end - start:.3f} seconds.\"", cls=CODE_STR_COLOR), ")"
			),
			data_prefix="17"
		),
		Pre(Code(""), data_prefix="18"),
		Pre(Code(""), data_prefix="19"),
		Pre(
			Code(
				Span("async", cls=CODE_KEYWORD_COLOR), " ",
				Span("def", cls=CODE_KEYWORD_COLOR), " ",
				Span("my_simulated_io_task", cls=CODE_FUNCTION_COLOR), "(id_: ",
				Span("int", cls=CODE_KEYWORD_COLOR), ") -> ",
				Span("str", cls=CODE_KEYWORD_COLOR), ":"
			),
			data_prefix="20"
		),
		Pre(
			Code(
				"	wait_time = ",
				Span("uniform", cls=CODE_FUNCTION_COLOR), "(1, 5)"
			),
			data_prefix="21"
		),
		Pre(
			Code(
				"	",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(",
				Span("f\"I/O task {id_} has started, waiting for {wait_time:.3f} seconds...\"", cls=CODE_STR_COLOR), ")"
			),
			data_prefix="22"
		),
		Pre(
			Code(
				"	",
				Span("await", cls=CODE_KEYWORD_COLOR), " ",
				Span("sleep", cls=CODE_FUNCTION_COLOR), "(wait_time)"
			),
			data_prefix="23"
		),
		Pre(
			Code(
				"	",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(",
				Span("f\"I/O task {id_} has finished!\"", cls=CODE_STR_COLOR), ")"
			),
			data_prefix="24"
		),
		Pre(
			Code(
				"	",
				Span("return", cls=CODE_KEYWORD_COLOR), " ",
				Span("f\"I/O task {id_} completed after {wait_time:.3f} seconds.\"", cls=CODE_STR_COLOR)
			),
			data_prefix="25"
		),
		Pre(Code(""), data_prefix="26"),
		Pre(Code(""), data_prefix="27"),
		Pre(
			Code(
				Span("if", cls=CODE_KEYWORD_COLOR), " ",
				Span("__name__", cls=CODE_BASE_COLOR), " == ",
				Span("\"__main__\"", cls=CODE_STR_COLOR), ":"
			),
			data_prefix="28"
		),
		Pre(
			Code(
				"	",
				Span("run(", cls=CODE_BASE_COLOR),
				Span("main())", cls=CODE_BASE_COLOR)
			),
			data_prefix="29"
		),
		cls="mockup-code w-full"
	)


def terminal_4():
	return Div(
		Pre(Code("python async_gather.py"), data_prefix="$", cls=CODE_BASE_COLOR),
		Pre(Code("I/O task 1 has started, waiting for 3.796 seconds..."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 2 has started, waiting for 2.187 seconds..."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 3 has started, waiting for 2.989 seconds..."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 4 has started, waiting for 1.781 seconds..."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 5 has started, waiting for 3.223 seconds..."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 6 has started, waiting for 1.474 seconds..."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 7 has started, waiting for 3.008 seconds..."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 8 has started, waiting for 2.403 seconds..."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 9 has started, waiting for 2.004 seconds..."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 10 has started, waiting for 2.734 seconds..."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 6 has finished!"), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 4 has finished!"), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 9 has finished!"), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 2 has finished!"), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 8 has finished!"), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 10 has finished!"), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 3 has finished!"), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 7 has finished!"), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 5 has finished!"), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 1 has finished!"), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 1 completed after 3.796 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 2 completed after 2.187 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 3 completed after 2.989 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 4 completed after 1.781 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 5 completed after 3.223 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 6 completed after 1.474 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 7 completed after 3.008 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 8 completed after 2.403 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 9 completed after 2.004 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 10 completed after 2.734 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("All tasks completed in 3.797 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		cls="mockup-code w-full"
	)


def code_5():
	return Div(
		Pre(
			Code(
				Span("# gather_even.py", cls=CODE_BASE_COLOR_50)
			),
			data_prefix="1"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("asyncio", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("run", cls=CODE_BASE_COLOR), ", ",
				Span("sleep", cls=CODE_BASE_COLOR), ", ",
				Span("gather", cls=CODE_BASE_COLOR)
			), 
			data_prefix="2"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("random", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("uniform", cls=CODE_BASE_COLOR)
			), 
			data_prefix="3"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("time", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("perf_counter", cls=CODE_BASE_COLOR)
			), 
			data_prefix="4"
		),
		Pre(Code(""), data_prefix="5"),
		Pre(Code(""), data_prefix="6"),
		Pre(
			Code(
				Span("async", cls=CODE_KEYWORD_COLOR), " ",
				Span("def", cls=CODE_KEYWORD_COLOR), " ",
				Span("main", cls=CODE_FUNCTION_COLOR), "() -> ",
				Span("None", cls=CODE_KEYWORD_COLOR), ":"
			),
			data_prefix="7"
		),
		Pre(
			Code(
				"	",
				"start = ",
				Span("perf_counter", cls=CODE_BASE_COLOR), "()"
			),
			data_prefix="8"
		),
		Pre(
			Code(
				"	",
				"tasks = []"
			),
			data_prefix="9"
		),
		Pre(
			Code(
				"	",
				Span("for", cls=CODE_KEYWORD_COLOR), " i ",
				Span("in", cls=CODE_KEYWORD_COLOR), " ",
				Span("range", cls=CODE_BUILT_IN_COLOR), "(10):"
			),
			data_prefix="10"
		),
		Pre(
			Code(
				"		",
				"tasks.append(",
				Span("my_simulated_io_task", cls=CODE_BASE_COLOR), "(i+1))"
			),
			data_prefix="11"
		),
		Pre(Code(""), data_prefix="12"),
		Pre(
			Code(
				"	",
				"results = ",
				Span("await", cls=CODE_KEYWORD_COLOR), " ",
				Span("gather", cls=CODE_FUNCTION_COLOR), "(*tasks)"
			),
			data_prefix="13"
		),
		Pre(
			Code(
				"	",
				Span("for", cls=CODE_KEYWORD_COLOR), " i, result ",
				Span("in", cls=CODE_KEYWORD_COLOR), " ",
				Span("enumerate", cls=CODE_BUILT_IN_COLOR), "(results, start=1):"
			),
			data_prefix="14"
		),
		Pre(
			Code(
				"		",
				Span("if", cls=CODE_KEYWORD_COLOR), " i % 2 == 0:"
			),
			data_prefix="15"
		),
		Pre(
			Code(
				"			",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(result)"
			),
			data_prefix="16"
		),
		Pre(
			Code(
				"	end = ",
				Span("perf_counter", cls=CODE_BASE_COLOR), "()"
			),
			data_prefix="17"
		),
		Pre(
			Code(
				"	",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(",
				Span("f\"All tasks completed in {end - start:.3f} seconds.\"", cls=CODE_STR_COLOR), ")"
			),
			data_prefix="18"
		),
		Pre(Code(""), data_prefix="19"),
		Pre(Code(""), data_prefix="20"),
		Pre(
			Code(
				Span("async", cls=CODE_KEYWORD_COLOR), " ",
				Span("def", cls=CODE_KEYWORD_COLOR), " ",
				Span("my_simulated_io_task", cls=CODE_FUNCTION_COLOR), "(id_: ",
				Span("int", cls=CODE_KEYWORD_COLOR), ") -> ",
				Span("str", cls=CODE_KEYWORD_COLOR), ":"
			),
			data_prefix="21"
		),
		Pre(
			Code(
				"	wait_time = ",
				Span("uniform", cls=CODE_FUNCTION_COLOR), "(1, 5)"
			),
			data_prefix="22"
		),
		Pre(
			Code(
				"	",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(",
				Span("f\"I/O task {id_} has started, waiting for {wait_time:.3f} seconds...\"", cls=CODE_STR_COLOR), ")"
			),
			data_prefix="23"
		),
		Pre(
			Code(
				"	",
				Span("await", cls=CODE_KEYWORD_COLOR), " ",
				Span("sleep", cls=CODE_FUNCTION_COLOR), "(wait_time)"
			),
			data_prefix="24"
		),
		Pre(
			Code(
				"	",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(",
				Span("f\"I/O task {id_} has finished!\"", cls=CODE_STR_COLOR), ")"
			),
			data_prefix="25"
		),
		Pre(
			Code(
				"	",
				Span("return", cls=CODE_KEYWORD_COLOR), " ",
				Span("f\"I/O task {id_} completed after {wait_time:.3f} seconds.\"", cls=CODE_STR_COLOR)
			),
			data_prefix="26"
		),
		Pre(Code(""), data_prefix="27"),
		Pre(Code(""), data_prefix="28"),
		Pre(
			Code(
				Span("if", cls=CODE_KEYWORD_COLOR), " ",
				Span("__name__", cls=CODE_BASE_COLOR), " == ",
				Span("\"__main__\"", cls=CODE_STR_COLOR), ":"
			),
			data_prefix="29"
		),
		Pre(
			Code(
				"	",
				Span("run(", cls=CODE_BASE_COLOR),
				Span("main())", cls=CODE_BASE_COLOR)
			),
			data_prefix="30"
		),
		cls="mockup-code w-full"
	)


def terminal_5():
	return Div(
		Pre(Code("python gather_even.py"), data_prefix="$", cls=CODE_BASE_COLOR),
		Pre(Code("..."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 5 has finished!"), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 2 completed after 4.186 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 4 completed after 2.549 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 6 completed after 3.022 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 8 completed after 3.176 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 10 completed after 2.765 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("All tasks completed in 4.611 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		cls="mockup-code w-full"
	)


def code_6():
	return Div(
		Pre(
			Code(
				Span("# task_group.py", cls=CODE_BASE_COLOR_50)
			),
			data_prefix="1"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("asyncio", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("run", cls=CODE_BASE_COLOR), ", ",
				Span("sleep", cls=CODE_BASE_COLOR), ", ",
				Span("TaskGroup", cls=CODE_BASE_COLOR)
			), 
			data_prefix="2"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("random", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("uniform", cls=CODE_BASE_COLOR)
			), 
			data_prefix="3"
		),
		Pre(
			Code(
				Span("from", cls=CODE_KEYWORD_COLOR), " ",
				Span("time", cls=CODE_BASE_COLOR), " ",
				Span("import", cls=CODE_KEYWORD_COLOR), " ",
				Span("perf_counter", cls=CODE_BASE_COLOR)
			), 
			data_prefix="4"
		),
		Pre(Code(""), data_prefix="5"),
		Pre(Code(""), data_prefix="6"),
		Pre(
			Code(
				Span("async", cls=CODE_KEYWORD_COLOR), " ",
				Span("def", cls=CODE_KEYWORD_COLOR), " ",
				Span("main", cls=CODE_FUNCTION_COLOR), "() -> ",
				Span("None", cls=CODE_KEYWORD_COLOR), ":"
			),
			data_prefix="7"
		),
		Pre(
			Code(
				"	",
				"start = ",
				Span("perf_counter", cls=CODE_BASE_COLOR), "()"
			),
			data_prefix="8"
		),
		Pre(
			Code(
				"	",
				"results = []"
			),
			data_prefix="9"
		),
		Pre(
			Code(
				"	",
				Span("async", cls=CODE_KEYWORD_COLOR), " ",
				Span("with", cls=CODE_KEYWORD_COLOR), " ",
				Span("TaskGroup", cls=CODE_BASE_COLOR), "() ",
				Span("as", cls=CODE_KEYWORD_COLOR), " tg:"
			),
			data_prefix="10"
		),
		Pre(
			Code(
				"		",
				Span("for", cls=CODE_KEYWORD_COLOR), " i ",
				Span("in", cls=CODE_KEYWORD_COLOR), " ",
				Span("range", cls=CODE_BUILT_IN_COLOR), "(10):"
			),
			data_prefix="11"
		),
		Pre(
			Code(
				"			",
				"tg.create_task("
			),
			data_prefix="12"
		),
		Pre(
			Code(
				"				",
				Span("my_simulated_io_task", cls=CODE_BASE_COLOR), "(i+1)"
			),
			data_prefix="13"
		),
		Pre(
			Code(
				"			).add_done_callback("
			),
			data_prefix="14"
		),
		Pre(
			Code(
				"				",
				Span("lambda", cls=CODE_KEYWORD_COLOR), " task, i=i+1: i % 2 == 0 ",
				Span("and", cls=CODE_KEYWORD_COLOR), " results.append(task.result())"
			),
			data_prefix="15"
		),
		Pre(
			Code(
				"			)"
			),
			data_prefix="16"
		),
		Pre(Code(""), data_prefix="17"),
		Pre(
			Code(
				"	",
				Span("for", cls=CODE_KEYWORD_COLOR), " result ",
				Span("in", cls=CODE_KEYWORD_COLOR), " results:"
			),
			data_prefix="18"
		),
		Pre(
			Code(
				"		",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(result)"
			),
			data_prefix="19"
		),
		Pre(Code(""), data_prefix="20"),
		Pre(
			Code(
				"	end = ",
				Span("perf_counter", cls=CODE_BASE_COLOR), "()"
			),
			data_prefix="21"
		),
		Pre(
			Code(
				"	",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(",
				Span("f\"All tasks completed in {end - start:.3f} seconds.\"", cls=CODE_STR_COLOR), ")"
			),
			data_prefix="22"
		),
		Pre(Code(""), data_prefix="23"),
		Pre(Code(""), data_prefix="24"),
		Pre(
			Code(
				Span("async", cls=CODE_KEYWORD_COLOR), " ",
				Span("def", cls=CODE_KEYWORD_COLOR), " ",
				Span("my_simulated_io_task", cls=CODE_FUNCTION_COLOR), "(id_: ",
				Span("int", cls=CODE_KEYWORD_COLOR), ") -> ",
				Span("str", cls=CODE_KEYWORD_COLOR), ":"
			),
			data_prefix="25"
		),
		Pre(
			Code(
				"	wait_time = ",
				Span("uniform", cls=CODE_FUNCTION_COLOR), "(1, 5)"
			),
			data_prefix="26"
		),
		Pre(
			Code(
				"	",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(",
				Span("f\"I/O task {id_} has started, waiting for {wait_time:.3f} seconds...\"", cls=CODE_STR_COLOR), ")"
			),
			data_prefix="27"
		),
		Pre(
			Code(
				"	",
				Span("await", cls=CODE_KEYWORD_COLOR), " ",
				Span("sleep", cls=CODE_FUNCTION_COLOR), "(wait_time)"
			),
			data_prefix="28"
		),
		Pre(
			Code(
				"	",
				Span("print", cls=CODE_BUILT_IN_COLOR), "(",
				Span("f\"I/O task {id_} has finished!\"", cls=CODE_STR_COLOR), ")"
			),
			data_prefix="29"
		),
		Pre(
			Code(
				"	",
				Span("return", cls=CODE_KEYWORD_COLOR), " ",
				Span("f\"I/O task {id_} completed after {wait_time:.3f} seconds.\"", cls=CODE_STR_COLOR)
			),
			data_prefix="30"
		),
		Pre(Code(""), data_prefix="31"),
		Pre(Code(""), data_prefix="32"),
		Pre(
			Code(
				Span("if", cls=CODE_KEYWORD_COLOR), " ",
				Span("__name__", cls=CODE_BASE_COLOR), " == ",
				Span("\"__main__\"", cls=CODE_STR_COLOR), ":"
			),
			data_prefix="33"
		),
		Pre(
			Code(
				"	",
				Span("run(", cls=CODE_BASE_COLOR),
				Span("main())", cls=CODE_BASE_COLOR)
			),
			data_prefix="34"
		),
		cls="mockup-code w-full"
	)


def terminal_6():
	return Div(
		Pre(Code("python task_group.py"), data_prefix="$", cls=CODE_BASE_COLOR),
		Pre(Code("..."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 1 has finished!"), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 10 completed after 1.499 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 2 completed after 1.625 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 6 completed after 2.022 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 8 completed after 2.171 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("I/O task 4 completed after 2.976 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		Pre(Code("All tasks completed in 4.806 seconds."), data_prefix=">", cls=CODE_STR_COLOR),
		cls="mockup-code w-full"
	)


@router("/blog")
async def blog(req: Request):
	print(req.url.path)
	created_at = datetime(2025, 9, 8, 0, 0, 0, tzinfo=UTC)
	created_at_str_date = created_at.strftime("%Y-%m-%d")
	now = datetime.now(UTC)
	return Div(
		H2("Blog", cls="text-xl"),
		Div(
			Figure(
				Img(src="/app/images/async.jpg", alt="Async banner", cls="object-cover object-center"),
				cls="h-24",
			),
			Div(
				Div(
					Button(
						language(),
						"(pt-BR) Traduzir para português brasileiro",
						cls="btn btn-soft btn-success btn-sm",
						hx_get="/blog/translate",
					),
				),
				Div(
					H2(
						"Improving Async IO in Python with examples",
						Br(),
						Div(
							Span(
								f"Created {format(created_at, now)}", data_tip=f"{created_at_str_date}",
								cls="tooltip tooltip-right"
							),
							cls="text-sm text-base-content/50",
						),
					),
					cls="card-title",
				),
				Div(
					"By improving, I mean focused on ",
					Span("running time and code alternatives. ", cls="font-bold"),
					"Let's start from the simple and then we go more complex.",
					cls="mt-2",
				),
				Div(
					"Async IO is a way to run many I/O-bound tasks concurrently (like network calls, database queries, file reads/writes) without blocking the program. This doesn’t create multiple threads; it runs on a ",
					Span("single event loop", cls="font-bold"),
					" that manages when tasks are paused and resumed.",
				),
				Div(
					"This content is not only bound to Python, but the examples will be in Python. I presume that Async IO features from Python are in other languages that support Async IO."
				),
				H3("Hello World!", cls="text-lg mt-2"),
				Div("This is how we define an async function and how to run it."),
				code_1(),
				terminal_1(),

				H3("Simulating IO with ", Code("sleep()"), cls="text-lg mt-4"),
				Div(
					"The following code will wait for a random time from 1 to 5 seconds and print the output of ",
					Code("my_simulated_io_task()"),
					". This is a simulation of a task that can take this amount of time; it could be a call to a network/database/file, for example.",
				),
				code_2(),
				terminal_2(),

				H3("Sync calls with Async IO functions", cls="text-lg mt-4"),
				Div("Let's start with the following code that has sync calls using async IO functions; you should avoid sync calls if possible. Sometimes, I see something similar to it, and I refactor it to have async calls. If the async functions are independent, you should call them asynchronously. I will show it in the next sections."),
				code_3(),
				Div("Note that ", Code("my_simulated_io_task()")," is defined as async, but the for loop of lines 9 and 10 calls the function synchronously; task 2 must wait for task 1 to be completed, and so on."),
				terminal_3(),
				Div("Check that the task order is kept (task 1, 2, 3, ...). It took more than 30 seconds, and it is the sum of all the tasks' times."),

				H3("Async calls with Async IO functions using ",  Code("gather()"), cls="text-lg mt-4"),
				Div("Now we are going to improve the performance of these tasks. The following code calls the functions asynchronously. We are also adding some prints to see these tasks running."),
				code_4(),
				terminal_4(),
				Div(
					"Note that the results are kept in order after the ",
					Code("gather()"),
					" call, but the tasks can finish in a different order due to the running time of each function. All tasks were completed ",
					Span("in 3.797 seconds because the tasks were run asynchronously", cls="font-bold"),
					". It is very close to the task 1, which took more time, 3.796 seconds. You can gain significant performance by running IO-bound tasks using Async IO. See the considerations sections that you should be aware of.",
				),

				H3("Async calls with results that need to be modified", cls="text-lg mt-4"),
				Div("There are cases where you need to modify the results of the async calls, in this case, I am showing an example where I want only the results of the tasks that have the pair indexes."),
				code_5(),
				Div("See that I needed to add an ", Code("if"), " statement at line 15 to print only tasks with pair indexes."),
				terminal_5(),
				Div("This works fine. Note again that the order of the results is kept (task 2, 4, 6, 8). But we can resolve everything in the first ", Code("for"), " as it is in the next section."),

				H3("Async calls with Async IO functions using ", Code("TaskGroup"), cls="text-lg mt-4"),
				Div(
					"You can see in the ", Code("async_gather.py"), " and ", Code("gather_even.py"), " that you are going to receive the results of the async functions only in the ", Code("await gather"), " call, and in the ", Code("code_5"), ", you need to use an ", Code("if"), " statement to filter out the odd tasks. We can change ", Code("gather_even.py"), " to resolve everything in the first ", Code("for"),
					" using ",
					A("TaskGroup", href="https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup", cls="link"),
					" in the following code:"
				),
				code_6(),
				Div(
					Code("add_done_callback()"),
					" will will be run after the task is completed, and this will add the result to the ", Code("results"), " list."
				),
				terminal_6(),
				Div(
					"Check that the tasks are added to the results list in a different order! In this case, the shorter task (task 10) is added first, and so on."
				),
				Div(
					"This approach is valid to avoid iterating over the results again to solve something that you need. If you only knew, ", Code("gather()"), " and you used it many times, you can see that ", Code("TaskGroup"), " can be an alternative to ", Code("gather()"), " in some cases because you can avoid loops to work the results."
				),

				H3("Considerations", cls="text-lg mt-4"),
				Div(
					"• Launching many tasks asynchronously could 'flood' services, and you can start having 'too many requests' kind of messages for your async calls.",
					Div("• To overcome this, send requests in batches, or even synchronously if running time is not a big issue.", cls="mt-2"),
					Div("• Take care about exceptions that can happen inside the tasks, depending on what you are solving, you must handle these exceptions.", cls="mt-2")
				),
				Div("ADD RISK OF USING PARAMS OF THE LOOP DIRECT INTO THE LAMBDA"),
				cls="card-body",
			),
			cls="card bg-base-300 shadow-md mt-4",
		),
	)


#Div("#python", cls="badge badge-soft"),
