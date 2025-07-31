from monsterui.all import Theme, ThemeRadii, fast_app, DividerLine, TextT, Container, NavBar, AT, H2, H5, UkIcon, UkIconLink, DivVStacked, DivRAligned, DivLAligned, Card, CardT, CardTitle, DivFullySpaced, Label, Grid
from fasthtml.common import Title, A, Div, Main, Link, Ul, Li, Span, Footer, Script, Body, Header, H3, P, Img
from app.icons import laptop_code, user_tie, graduation_cap, newspaper, blog, envelope, whatsapp, linkedin, github, python, globe

from app.views import card
from app.content import NECC_CONTENT, TELNYX_CONTENT, MARTIAN_CONTENT, PINTEREST_CONTENT, SEEBOT_CONTENT, EARLYSEC_CONTENT, MASTERS_CONTENT, GRADUATION_CONTENT, PAPER_1, PAPER_2
from app.settings import get_settings

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
# 	Link(rel="stylesheet", href="app/css/main.css"),
# 	*Theme.green.headers(radii=ThemeRadii.md),
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



@router("/")  # type: ignore[misc]
async def get():  # type: ignore[no-untyped-def]  # noqa: ANN201
	return (
		Title("Allainclair Flausino dos Santos"),
		Body(
			_header(),
			Div(
				Div(
					Div(
						Div(
							Div("Total experience", cls="stat-title"),
							Div("10yrs+", cls="stat-value"),
							cls="stat",
						),
						Div(
							Div("Work for US based companies", cls="stat-title"),
							Div("6yrs+", cls="stat-value"),
							cls="stat",
						),
						Div(
							Div(globe(), cls="stat-figure"),
							Div("Main Experience", cls="stat-title"),
							Div("Backend", cls="stat-value"),
							cls="stat",
						),
						Div(
							Div(python(), cls="stat-figure"),
							Div("Main Programming Language", cls="stat-title"),
							Div("Python", cls="stat-value"),
							cls="stat",
						),
						cls="stats stats-vertical sm:stats-vertical md:stats-vertical lg:stats-horizontal xl:stats-horizontal",
					),
					cls="flex flex-wrap items-center justify-center mx-auto"
				),
				H3("Professional Experience", id="professional-experience", cls="mt-5 text-xl text-primary font-bold"),
				Div(
					card(
						"Backend Software Engineer at Telnyx",
						"Jan 2025 - Present (less 1 than yr)",
						["I have been developing backend web APIs for SMS messaging management."],
						["Python", "FastAPI", "Docker", "PostgreSQL", "Pytest", "Grafana"],
						"/app/logos/telnyx.svg",
						"opacity-20",
						checked=True,
					),
					card(
						"Software Engineer at New England Center for Children",
						"Aug 2023 - Dec 2024 (1 yr 5 mos)",
						["I worked on creating Python FastAPI/Quart/JavaScript apps with MySQL to manage data."],
						["Python", "FastAPI", "Docker", "MySQL", "Pytest", "JavaScript", "Quart"],
						"/app/logos/necc.svg",
						"opacity-3",
					),
					card(
						"Software Engineer at Martian",
						"Apr 2024 - Jul 2024 (5 mos)",
						MARTIAN_CONTENT,
						["Python", "FastAPI", "Litestar", "Docker", "Pytest", "Jinja", "MongoDB"],
						"/app/logos/martian.png",
						"opacity-10",
					),
					card(
						"Backend Software Engineer at Shipwell",
						"Sep 2022 - Jul 2023 (11 mos)",
						["Designing, creating, and maintaining a backend service to integrate load boards across North America."],
						["Python", "FastAPI", "Docker", "PostgreSQL", "FastAPI", "Pytest", "SQLAlchemy", "AWS", "RabbitMQ", "Redis"],
						"/app/logos/shipwell-2.svg",
						"opacity-5",
					),
					card(
						"Software Engineer at Pinterest",
						"Sep 2019 - Jul 2022 (2 yrs 11 mos)",
						PINTEREST_CONTENT,
						["Python", "SQL", "Flask", "Docker", "AWS", "React.JS", "Pytest", "Pandas"],
						"/app/logos/pinterest.png",
						"opacity-5",
					),
					card(
						"Software Engineer at BairesDev",
						"Sep 2019 - Jul 2022 (2 yrs 11 mos)",
						["We created screening processes for new employees, and we also helped some colleagues with mentorships. I interviewed many candidates to be Python-focused software engineers."],
						["Python"],
						"/app/logos/bairesdev.png",
						"opacity-20",
					),
					card(
						"Assistant Professor at State University of Maringá",
						"Apr 2019 - Oct 2019 (7 mos)",
						["I ministered the following subjects: • Algorithms and Data Structures. • Relational Database. • Multi and Hypermedia Systems. • Algorithm Analysis and Graph Theory. • Object-Oriented Programming."],
						["Python", "SQL", "C", "Java"],
						"/app/logos/uem.png",
						"opacity-15",
					),
					card(
						"Software Engineer at Seebot",
						"Oct 2015 - Sep 2019 (3 yrs 11 mos)",
						SEEBOT_CONTENT,
						["Python", "Gevent", "Linux", "Graph Theory", "Systemd"],
						"/app/logos/seebot.png",
						"opacity-5",
					),
					card(
						"Data Scientist at EarlySec",
						"Jun 2018 - Mar 2019 (10 mos)",
						EARLYSEC_CONTENT,
						["Python", "Java", "Natural Language Processing", "Elasticsearch", "Kafka", "Pytest"],
					),
					cls=(
						"grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 "
						"lg:grid-cols-2 xl:grid-cols-2 gap-4 mt-3"
					),
				),
				H3("Projects", id="projects", cls="mt-5 text-xl text-primary font-bold"),
				Div(
					card(
						"Akingressos (PT-BR)",
						"2024 - Present",
						["Website that aggregates events from different websites and shows them in a single place: ", A("akingressos.com.br", cls="link", href="https://akingressos.com.br", target="_blank")],
						["Python", "HTMX", "FastHTML", "MonsterUI"],
					),
					card(
						"TicTec (PT-BR)",
						"2025 - Present",
						["Website that aggregates Brazilian tech influencers: ", A("tt.allainclair.com.br (PT-BR)", cls="link", href="https://tt.allainclair.com", target="_blank")],
						["Python", "HTMX", "FastHTML", "DaisyUI"],
					),
					cls=(
						"grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 "
						"lg:grid-cols-2 xl:grid-cols-2 gap-4 mt-3"
					),
				),
				H3("Education", id="education", cls="mt-5 text-xl text-primary font-bold"),
				Div(
					card(
						"Master's Degree in Computer Science at State University of Maringá",
						"2014 - 2016 (2 yrs)",
						["Major in Combinatorial Optimization, Bus Driver Schedule Problem: Algorithms based on Variable Neighborhood Search (VNS) metaheuristic applied in the Bus Driver Schedule Problem."],
						["Python", "Graph Theory"],
					),
					card(
						"Bachelor's Degree in Computer Science at State University of Maringá",
						"2010 - 2013 (4 yrs)",
						["Major in Computer Science, Combinatorial Optimization, Feedback Arc Set Problem: A genetic algorithm for the Feedback Arc Set Problem."],
						["Python", "Graph Theory"],
					),
					cls=(
						"grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 "
						"lg:grid-cols-2 xl:grid-cols-2 gap-4 mt-3"
					),
				),
				H3("Scientific Papers Published ", id="scientific-papers", cls="mt-5 text-xl text-primary font-bold"),
				Div(
					card(
						"Journal of Universal Computer Science",
						"May 2017",
						["Solving a Large Real-world Bus Driver Scheduling Problem with a Multi-assignment based Heuristic Algorithm: ",  A("files", href="https://www.jucs.org/jucs_23_5/solving_a_large_real/", cls="link", target="_blank")],
						[],
					),
					card(
						"XLVIII SBPO - Simpósio Brasileiro de Pesquisa Operacional (PT-BR)",
						"Sep 2016",
						["Algoritmos baseados na meta-heurística VNS aplicados ao Problema de Escalonamento de Motoristas de Ônibus: ", A("PDF", href="http://www.din.uem.br/sbpo/sbpo2016/pdf/156702.pdf", cls="link", target="_blank")],
						[],
					),
					cls=(
						"grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 "
						"lg:grid-cols-2 xl:grid-cols-2 gap-4 mt-3"
					),
				),
				cls="container mx-auto gap-4 mt-4 w-11/12",
			),
		),
	)

def _header() -> Header:
	return Header(
		Div(
			A(
				Div(
					H2("Allainclair", cls="text-3xl font-bold"),
					H3("Software Engineer", cls="text-xl"),
				href="/",
				),
			),

			Div(
				A(
					user_tie(),
					Div("Professional Experience", cls="ml-2"),
					role="tab",
					href="#professional-experience",
					cls="tab",
				),
				A(
					laptop_code(),
					Div("Projects", cls="ml-2"),
					role="tab",
					href="#projects",
					cls="tab",
				),
				A(
					graduation_cap(),
					Div("Education", cls="ml-2"),
					role="tab",
					href="#education",
					cls="tab",
				),
				A(
					newspaper(),
					Div("Scientific Papers", cls="ml-2"),
					role="tab",
					href="#scientific-papers",
					cls="tab",
				),
				A(
					blog(),
					Div("Blog", cls="ml-2"),
					role="tab",
					href="#",
					cls="tab tab-disabled",
				),
				role="tablist",
				cls="tabs tabs-box items-center my-2",
			),

			Ul(
				Li(A(envelope(), cls="tooltip tooltip-bottom", data_tip="Email")),
				Li(A(linkedin(), cls="tooltip tooltip-bottom", data_tip="LinkedIn")),
				Li(A(github(), cls="tooltip tooltip-bottom", data_tip="GitHub")),
				Li(A(whatsapp(), cls="tooltip tooltip-bottom", data_tip="WhatsApp")),
				cls="menu menu-horizontal",
			),
			cls="container mx-auto flex flex-wrap justify-between mt-4 w-11/12",
		)
	)
