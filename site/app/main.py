from starlette.requests import Request
from fasthtml.common import Title, A, Div, Link, Script, Body, Header, H3, cookie, fast_app, FT, Img, Input, P, H2
from app.icons import python, business_time, flag_usa, server
from uuid import uuid4

from app.views import header
from app.content import (
	get_necc_content, get_telnyx_content, get_martian_content, get_pinterest_content, 
	get_seebot_content, get_earlysec_content,
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
async def get(
	req: Request,
	user_language: str | None = None,
	tab_active: str | None = None,
):  # type: ignore[no-untyped-def]  # noqa: ANN201
	user_language = get_user_language(req, user_language)
	return (
		Title("Allainclair Flausino dos Santos"),
		Body(
			*_body_content(user_language, tab_active or "professional-experience"),
			id="body-content",
		),
	), cookie("user_language", user_language)


@router("/body-content")  # type: ignore[misc]
async def get(language: str):  # type: ignore[no-untyped-def]  # noqa: ANN201
	# TODO: Add if the language is present: language: str | None = None
	return _body_content(language), cookie("user_language", language)


def _body_content(user_language: str, tab_active: str = "professional-experience") -> tuple[Header, Div]:
	return (
		header(user_language, "/body-content", tab_active),
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
			H3(
				i18n("Professional Experience", user_language),
				id="professional-experience",
				cls="mt-5 text-xl text-primary font-bold",
			),
			Div(
				_card(
					i18n("Backend Software Engineer at Telnyx", user_language),
					i18n("Jan 2025 - Present (less 1 than yr)", user_language),
					get_telnyx_content(user_language),
					["Python", "FastAPI", "Docker", "PostgreSQL", "Pytest", "Grafana"],
					"/app/logos/telnyx.svg",
					"opacity-20",
					checked=True,
				),
				_card(
					i18n("Software Engineer at New England Center for Children", user_language),
					i18n("Aug 2023 - Dec 2024 (1 yr 5 mos)", user_language),
					get_necc_content(user_language),
					["Python", "FastAPI", "Docker", "MySQL", "Pytest", "JavaScript", "Quart"],
					"/app/logos/necc.svg",
					"opacity-3",
				),
				_card(
					i18n("Software Engineer at Martian", user_language),
					i18n("Apr 2024 - Jul 2024 (5 mos)", user_language),
					get_martian_content(user_language),
					["Python", "FastAPI", "Litestar", "Docker", "Pytest", "Jinja", "MongoDB"],
					"/app/logos/martian.png",
					"opacity-10",
				),
				_card(
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
				_card(
					i18n("Software Engineer at Pinterest", user_language),
					i18n("Sep 2019 - Jul 2022 (2 yrs 11 mos)", user_language),
					get_pinterest_content(user_language),
					["Python", "SQL", "Flask", "Docker", "AWS", "React.JS", "Pytest", "Pandas"],
					"/app/logos/pinterest.png",
					"opacity-5",
				),
				_card(
					i18n("Software Engineer at BairesDev", user_language),
					i18n("Sep 2019 - Jul 2022 (2 yrs 11 mos)", user_language),
					[i18n(
						"• Created screening processes for new employees, and we also helped some colleagues with mentorships. I interviewed many candidates to be Python-focused software engineers.",
						user_language)],
					["Python"],
					"/app/logos/bairesdev.png",
					"opacity-20",
				),
				_card(
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
				_card(
					i18n("Software Engineer at Seebot", user_language),
					i18n("Oct 2015 - Sep 2019 (3 yrs 11 mos)", user_language),
					get_seebot_content(user_language),
					["Python", "Gevent", "Linux", "Graph Theory", "Systemd"],
					"/app/logos/seebot.png",
					"opacity-5",
				),
				_card(
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
				_card(
					"Akingressos (pt-BR)",
					i18n("2024 - Present", user_language),
					[
						i18n(
							"Website that aggregates events from different websites and shows them in a single place: ",
							user_language),
						A("akingressos.com.br", cls="link", href="https://akingressos.com.br", target="_blank")],
					["Python", "HTMX", "FastHTML", "MonsterUI"],
				),
				_card(
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
				_card(
					i18n("Master's Degree in Computer Science at State University of Maringá", user_language),
					i18n("2014 - 2016 (3 yrs)", user_language),
					[
						i18n(
							"Major in Combinatorial Optimization, Bus Driver Schedule Problem: Algorithms based on Variable Neighborhood Search (VNS) metaheuristic applied in the Bus Driver Schedule Problem.",
							user_language)
					],
					["Python", "Graph Theory"],
				),
				_card(
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
				_card(
					"Journal of Universal Computer Science",
					i18n("May 2017", user_language),
					["Solving a Large Real-world Bus Driver Scheduling Problem with a Multi-assignment based Heuristic Algorithm: ",
					 A("files", href="https://www.jucs.org/jucs_23_5/solving_a_large_real/", cls="link",
					   target="_blank")],
					[],
				),
				_card(
					"XLVIII SBPO - Simpósio Brasileiro de Pesquisa Operacional (pt-BR)",
					i18n("Sep 2016", user_language),
					["Algoritmos baseados na meta-heurística VNS aplicados ao Problema de Escalonamento de Motoristas de Ônibus: ",
					 A("PDF", href="http://www.din.uem.br/sbpo/sbpo2016/pdf/156702.pdf", cls="link", target="_blank")],
					[],
				),
				_card(
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

def _card(
	title: str,
	period: str,
	contents: list[FT | str],
	techs: list[str],
	logo_path: str | None = None,
	logo_opacity: str | None = None,
	checked: bool = False,
) -> Div:
	imgs = [Img(src=logo_path, cls=f"logo-img {logo_opacity}", alt="Company logo")] if logo_path else []
	return Div(
		*imgs,
		Div(
			Input(type="checkbox", name=str(uuid4()), checked=checked),
			Div(
				H2(title, cls="card-title"),
				P(period, cls="text-sm text-base-content/70"),
				cls="collapse-title",
			),
			Div(
				*contents,
				Div(*[Div(tech, cls="badge") for tech in techs], cls="flex flex-wrap gap-2 mt-2"),
				cls="collapse-content",
			),
			cls="collapse collapse-arrow",
		),
		cls=f"card bg-base-300 card-md shadow-md",
	)
