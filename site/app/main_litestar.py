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


@get(path="/education")
async def get_education() -> Template:
	return HTMXTemplate(template_name="education.html.jinja2")


@get(path="/professional-experience")
async def get_professional_experience() -> Template:
	return HTMXTemplate(template_name="professional-experience.html.jinja2")


@get(path="/projects")
async def get_projects() -> Template:
	return HTMXTemplate(template_name="projects.html.jinja2")


app = Litestar(
	route_handlers=[
		get_index,
		get_education,
		get_professional_experience,
		get_projects,
		create_static_files_router(path="/images", directories=["app/images"]),
	],
	debug=True,
	request_class=HTMXRequest,
	template_config=TemplateConfig(
		directory=Path("app/templates"),
		engine=JinjaTemplateEngine,
	),
)
