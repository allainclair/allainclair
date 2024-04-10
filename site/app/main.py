from litestar import Litestar, Response, get
from litestar.response import Template
from litestar.static_files.config import create_static_files_router
from litestar.contrib.htmx.request import HTMXRequest
from litestar.template.config import TemplateConfig
from litestar.contrib.jinja import JinjaTemplateEngine

from litestar.contrib.htmx.response import HTMXTemplate
from pathlib import Path


@get(path="/")
async def get_index() -> Template:
	# Check if it is sync or async.
	return HTMXTemplate(template_name="index.html")

app = Litestar(
	route_handlers=[
		get_index,
		create_static_files_router(path="/images", directories=["app/images"]),
		create_static_files_router(path="/js", directories=["app/js"]),
	],
	debug=True,
	request_class=HTMXRequest,
	template_config=TemplateConfig(
		directory=Path("app/templates"),
		engine=JinjaTemplateEngine,
	),
)
