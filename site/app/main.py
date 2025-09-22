from monsterui.all import fast_app, H2
from fasthtml import fastapp
from starlette.requests import Request
from fasthtml.common import Title, A, Button, Div, Link, Ul, Li, Script, Body, Header, H3, cookie, parsed_date
from app.icons import laptop_code, user_tie, graduation_cap, newspaper, blog, envelope, whatsapp, linkedin, github, python, globe, file_user, business_time, flag_usa, server, language

from app.views import card
from app.content import (
	get_necc_content, get_telnyx_content, get_martian_content, get_pinterest_content, 
	get_seebot_content, get_earlysec_content, get_masters_content, get_graduation_content, 
	get_paper_1, PAPER_2
)
from app.settings import get_settings
from app.blog.views import router as router_blog
from app.language import get_user_language
from app.i18n import i18n

GTAG_2 = f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());

gtag('config', '{get_settings().google_analytics_id}');
"""

headers_prod = headers_dev = None

env = get_settings().env

# COMMON_HEADERS = (
# 	# Link(rel="icon", href="app/assets/favicon/favicon.ico"),
# )

COMMON_HEADERS = (Link(href="/dist/output.css", rel="stylesheet"),)

if env == "prod" and get_settings().google_analytics_id:
	headers_prod = (
		Script(
			src=f"https://www.googletagmanager.com/gtag/js?id={get_settings().google_analytics_id}"
		),
		Script(GTAG_2),
		*COMMON_HEADERS,
		# Add Icons
	)

else:
	headers_dev = (*COMMON_HEADERS,)

headers = headers_dev or headers_prod

app, router = fast_app(hdrs=headers, live=env == "dev", pico=False)
router_blog.to_app(app)


@router("/")  # type: ignore[misc]
async def get(req: Request, user_language: str | None = None):  # type: ignore[no-untyped-def]  # noqa: ANN201
	user_language = get_user_language(req, user_language)
	return (
		Title("Allainclair Flausino dos Santos"),
		Body(*_body_content(user_language), id="main-body-content"),
	), cookie("user_language", user_language)



@router("/main-body-content")  # type: ignore[misc]
async def get(language: str):  # type: ignore[no-untyped-def]  # noqa: ANN201
	print(f"Main body {language=}")
	return _body_content(language), cookie("user_language", language)


def _header(user_language: str, path: str) -> Header:
	if user_language == "en":
		button_lang = Button(
			language(),
			"pt-BR",
			cls="btn btn-soft btn-info btn-sm tooltip tooltip-left",
			data_tip="Traduzir para Português",
			hx_get=f"{path}main-body-content?language=pt",
			hx_target="#main-body-content",
		)
	else:
		button_lang = Button(
			language(),
			"en",
			cls="btn btn-soft btn-info btn-sm tooltip tooltip-left",
			data_tip="Translate to English",
			hx_get=f"{path}main-body-content?language=en",
			hx_target="#main-body-content",
		)

	return Header(
		Div(
			Div(
				Ul(
					Li(A(envelope(), cls="tooltip tooltip-bottom", data_tip="Email", href="mailto:allainclair.com")),
					Li(A(linkedin(), cls="tooltip tooltip-bottom", data_tip="LinkedIn",
						 href="https://www.linkedin.com/in/allainclair/", target="_blank")),
					Li(A(github(), cls="tooltip tooltip-bottom", data_tip="GitHub",
						 href="https://github.com/allainclair/", target="_blank")),
					Li(A(whatsapp(), cls="tooltip tooltip-bottom", data_tip="WhatsApp",
						 href="https://wa.me/5544997191891?text=Olá Allainclair", target="_blank")),
					Li(A(file_user(), cls="tooltip tooltip-bottom", data_tip="Resume PDF",
						 href="/app/docs/allainclair-resume.pdf", target="_blank")),
					cls="menu menu-horizontal",
				),
				button_lang,
				cls="container mx-auto flex flex-wrap justify-between items-center w-11/12",
			),
			cls="w-full bg-neutral shadow-md",
		),

		Div(
			Div(
				A(
					Div(
						H2("Allainclair Flausino dos Santos", cls="text-3xl font-bold flex items-center justify-center"),
						H3(i18n("Software Engineer", user_language), cls="text-xl text-primary flex items-center justify-center"),
					),
					href="/",
				),
				cls="flex justify-center gap-2",
			),

			Div(
			Div(
				A(
					user_tie(),
					Div(i18n("Professional Experience", user_language), cls="ml-2"),
					role="tab",
					href="/#professional-experience",
					cls="tab",
				),
				A(
					laptop_code(),
					Div(i18n("Projects", user_language), cls="ml-2"),
					role="tab",
					href="#projects",
					cls="tab",
				),
				A(
					graduation_cap(),
					Div(i18n("Education", user_language), cls="ml-2"),
					role="tab",
					href="#education",
					cls="tab",
				),
				A(
					newspaper(),
					Div(i18n("Scientific Papers", user_language), cls="ml-2"),
					role="tab",
					href="#scientific-papers",
					cls="tab",
				),
				A(
					blog(),
					Div("Blog", cls="ml-2"),
					role="tab",
					#href="/blog",
					hx_get=f"/blog",
					hx_target="#main-content",
					hx_push_url="true",
					cls="tab tab-disabled",
				),
				role="tablist",
				cls="tabs tabs-box justify-center my-2",
			),
				cls="flex justify-center",
			),

			cls="container mx-auto mt-4 w-11/12",
		),
	)


def _body_content(user_language: str) -> tuple[Header, Div]:
	return (
		_header(user_language, "/"),
		Div(
			Div(
				Div(
					Div(
						Div(business_time(), cls="stat-figure text-success"),
						Div(i18n("Total experience", user_language), cls="stat-title"),
						Div(i18n("10 yrs+", user_language), cls="stat-value text-success"),
						Div(i18n("Mainly in Software Engineer", user_language), cls="stat-desc"),
						cls="stat",
					),
					Div(
						Div(flag_usa(), cls="stat-figure text-error"),
						Div(i18n("Work for US-based companies", user_language), cls="stat-title"),
						Div(i18n("6 yrs+", user_language), cls="stat-value text-error"),
						Div(i18n("Across 6 different companies", user_language), cls="stat-desc"),
						cls="stat",
					),
					cls="stats stats-vertical sm:stats-vertical md:stats-vertical lg:stats-horizontal xl:stats-horizontal",
				),
				Div(
					Div(
						Div(server(), cls="stat-figure text-info"),
						Div(i18n("Main Experience", user_language), cls="stat-title"),
						Div("Web Backend", cls="stat-value text-info"),
						Div(i18n("Distributed Systems, Microservices, SQL", user_language), cls="stat-desc"),
						cls="stat",
					),
					Div(
						Div(python(), cls="stat-figure text-warning"),
						Div(i18n("Main Programming Language", user_language), cls="stat-title"),
						Div("Python", cls="stat-value text-warning"),
						Div(i18n("Others: JavaScript, Java, Go, Shell", user_language), cls="stat-desc"),
						cls="stat",
					),
					cls="stats stats-vertical sm:stats-vertical md:stats-vertical lg:stats-horizontal xl:stats-horizontal",
				),
				cls="flex flex-wrap items-center justify-center mx-auto"
			),
			H3(i18n("Professional Experience", user_language), id="professional-experience",
			   cls="mt-5 text-xl text-primary font-bold"),
			Div(
				card(
					i18n("Backend Software Engineer at Telnyx", user_language),
					i18n("Jan 2025 - Present (less 1 than yr)", user_language),
					get_telnyx_content(user_language),
					["Python", "FastAPI", "Docker", "PostgreSQL", "Pytest", "Grafana"],
					"/app/logos/telnyx.svg",
					"opacity-20",
					checked=True,
				),
				card(
					i18n("Software Engineer at New England Center for Children", user_language),
					i18n("Aug 2023 - Dec 2024 (1 yr 5 mos)", user_language),
					get_necc_content(user_language),
					["Python", "FastAPI", "Docker", "MySQL", "Pytest", "JavaScript", "Quart"],
					"/app/logos/necc.svg",
					"opacity-3",
				),
				card(
					i18n("Software Engineer at Martian", user_language),
					i18n("Apr 2024 - Jul 2024 (5 mos)", user_language),
					get_martian_content(user_language),
					["Python", "FastAPI", "Litestar", "Docker", "Pytest", "Jinja", "MongoDB"],
					"/app/logos/martian.png",
					"opacity-10",
				),
				card(
					i18n("Backend Software Engineer at Shipwell", user_language),
					i18n("Sep 2022 - Jul 2023 (11 mos)", user_language),
					[
						i18n(
							"• Developed backend microservices integrating 3 freight load board APIs, streamlining logistics workflows across North America.",
							user_language),
					],
					["Python", "FastAPI", "Docker", "PostgreSQL", "FastAPI", "Pytest", "SQLAlchemy", "AWS", "RabbitMQ",
					 "Redis"],
					"/app/logos/shipwell-2.svg",
					"opacity-5",
				),
				card(
					i18n("Software Engineer at Pinterest", user_language),
					i18n("Sep 2019 - Jul 2022 (2 yrs 11 mos)", user_language),
					get_pinterest_content(user_language),
					["Python", "SQL", "Flask", "Docker", "AWS", "React.JS", "Pytest", "Pandas"],
					"/app/logos/pinterest.png",
					"opacity-5",
				),
				card(
					i18n("Software Engineer at BairesDev", user_language),
					i18n("Sep 2019 - Jul 2022 (2 yrs 11 mos)", user_language),
					[i18n(
						"• Created screening processes for new employees, and we also helped some colleagues with mentorships. I interviewed many candidates to be Python-focused software engineers.",
						user_language)],
					["Python"],
					"/app/logos/bairesdev.png",
					"opacity-20",
				),
				card(
					i18n("Assistant Professor at State University of Maringá", user_language),
					i18n("Apr 2019 - Oct 2019 (7 mos)", user_language),
					[i18n(
						"• Ministered the following subjects: Algorithms and Data Structures, Relational Database, Multi and Hypermedia Systems, Algorithm analysis and Graph Theory, Object-Oriented Programming.",
						user_language)
					],
					["Python", "SQL", "C", "Java"],
					"/app/logos/uem.png",
					"opacity-15",
				),
				card(
					i18n("Software Engineer at Seebot", user_language),
					i18n("Oct 2015 - Sep 2019 (3 yrs 11 mos)", user_language),
					get_seebot_content(user_language),
					["Python", "Gevent", "Linux", "Graph Theory", "Systemd"],
					"/app/logos/seebot.png",
					"opacity-5",
				),
				card(
					i18n("Data Scientist at EarlySec", user_language),
					i18n("Jun 2018 - Mar 2019 (10 mos)", user_language),
					get_earlysec_content(user_language),
					["Python", "Java", "Natural Language Processing", "Elasticsearch", "Kafka", "Pytest"],
				),
				cls=(
					"grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 "
					"lg:grid-cols-2 xl:grid-cols-2 gap-4 mt-3"
				),
			),
			H3(i18n("Projects", user_language), id="projects", cls="mt-5 text-xl text-primary font-bold"),
			Div(
				card(
					"Akingressos (pt-BR)",
					i18n("2024 - Present", user_language),
					[
						i18n(
							"Website that aggregates events from different websites and shows them in a single place: ",
							user_language),
						A("akingressos.com.br", cls="link", href="https://akingressos.com.br", target="_blank")],
					["Python", "HTMX", "FastHTML", "MonsterUI"],
				),
				card(
					"TicDec (pt-BR)",
					i18n("2025 - Present", user_language),
					[
						i18n("Website that aggregates Brazilian tech influencers: ", user_language),
						A("tid.dev.br (PT-BR)", cls="link", href="https://tic.dev.br", target="_blank")
					],
					["Python", "HTMX", "FastHTML", "DaisyUI"],
				),
				cls=(
					"grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 "
					"lg:grid-cols-2 xl:grid-cols-2 gap-4 mt-3"
				),
			),
			H3(i18n("Education", user_language), id="education", cls="mt-5 text-xl text-primary font-bold"),
			Div(
				card(
					i18n("Master's Degree in Computer Science at State University of Maringá", user_language),
					i18n("2014 - 2016 (3 yrs)", user_language),
					[
						i18n(
							"Major in Combinatorial Optimization, Bus Driver Schedule Problem: Algorithms based on Variable Neighborhood Search (VNS) metaheuristic applied in the Bus Driver Schedule Problem.",
							user_language)
					],
					["Python", "Graph Theory"],
				),
				card(
					i18n("Bachelor's Degree in Computer Science at State University of Maringá", user_language),
					i18n("2010 - 2013 (4 yrs)", user_language),
					[
						i18n(
							"Major in Computer Science, Combinatorial Optimization, Feedback Arc Set Problem: A genetic algorithm for the Feedback Arc Set Problem.",
							user_language),
					],
					["Python", "Graph Theory"],
				),
				cls=(
					"grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 "
					"lg:grid-cols-2 xl:grid-cols-2 gap-4 mt-3"
				),
			),
			H3(
				i18n("Scientific Papers Published", user_language),
				id="scientific-papers",
				cls="mt-5 text-xl text-primary font-bold",
			),
			Div(
				card(
					"Journal of Universal Computer Science",
					i18n("May 2017", user_language),
					["Solving a Large Real-world Bus Driver Scheduling Problem with a Multi-assignment based Heuristic Algorithm: ",
					 A("files", href="https://www.jucs.org/jucs_23_5/solving_a_large_real/", cls="link",
					   target="_blank")],
					[],
				),
				card(
					"XLVIII SBPO - Simpósio Brasileiro de Pesquisa Operacional (pt-BR)",
					i18n("Sep 2016", user_language),
					["Algoritmos baseados na meta-heurística VNS aplicados ao Problema de Escalonamento de Motoristas de Ônibus: ",
					 A("PDF", href="http://www.din.uem.br/sbpo/sbpo2016/pdf/156702.pdf", cls="link", target="_blank")],
					[],
				),
				card(
					"17th International Conference on Enterprise Information Systems (ICEIS-2015)",
					"Jan 2015",
					["Combining Heuristic and Utility Function for Fair Train Crew Rostering: ",
					 A("PDF", href="https://www.scitepress.org/PublishedPapers/2015/53645/53645.pdf", cls="link",
					   target="_blank")],
					[],
				),
				cls=(
					"grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 "
					"lg:grid-cols-2 xl:grid-cols-2 gap-4 mt-3"
				),
			),
			id="main-content",
			cls="container mx-auto gap-4 mt-4 w-11/12",
		),
	)