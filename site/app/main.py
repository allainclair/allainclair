from monsterui.all import Theme, ThemeRadii, fast_app, DividerLine, TextT, Container, NavBar, AT, H2, H3, H5, UkIcon, UkIconLink, DivVStacked, DivRAligned, DivLAligned, Card, CardT, CardTitle, DivFullySpaced, Label, Grid
from fasthtml.common import Title, A, Div, Main, Link, Ul, Li, Span, Footer, Script

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

COMMON_HEADERS = (
	# Link(rel="icon", href="app/assets/favicon/favicon.ico"),
	Link(rel="stylesheet", href="app/css/main.css"),
	*Theme.green.headers(radii=ThemeRadii.md),
)

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
		Container(
			NavBar(
				A(
					DivRAligned(
						Div(UkIcon("laptop-minimal")),
						Div(H5("Professional Experience")),
						cls="space-x-2",
					),
					cls=AT.text,
					href="#professional-experience"
				),
				A(
					DivRAligned(
						Div(UkIcon("folder-git-2")),
						Div(H5("Projects")),
						cls="space-x-2",
					),
					cls=AT.text,
					href="#projects"
				),
				A(
					DivRAligned(
						Div(UkIcon("graduation-cap")),
						Div(H5("Education")),
						cls="space-x-2",
					),
					cls=AT.text,
					href="#education"
				),
				A(
					DivRAligned(
						Div(UkIcon("newspaper")),
						Div(H5("Scientific Papers")),
						cls="space-x-2",
					),
					cls=AT.text,
					href="#scientific-papers",
				),
				A(
					DivRAligned(
						Div(UkIcon("pen")),
						Div(H5("Blog")),
						cls="space-x-2",
					),
					cls=AT.text
				),
				UkIconLink("linkedin", href="https://www.linkedin.com/in/allainclair/"),
				UkIconLink("github", href="https://github.com/allainclair"),
				UkIconLink("mail", href="mailto:allainclair@gmail.com"),
				brand=A(
					H2("Allainclair", cls=TextT.primary),
					H3("Software Engineer", cls=TextT.primary),
					cls=AT.reset,
				),
			),

			Main(
				DivVStacked(
					Div(H3("Professional Experience", cls=TextT.primary), id="professional-experience"),
					Grid(
						card(
							TELNYX_CONTENT,
							"Backend Software Engineer at ",
							"Telnyx",
							"https://telnyx.com/",
							"Jan 2025 - Present (less 1 yr)",
							["Python", "FastAPI", "Docker", "PostgreSQL", "Pytest"],
							"experience-card-telnyx",
						),
						card(
							NECC_CONTENT,
							"Software Engineer at ",
							"The New England Center for Children",
							"https://www.necc.org/",
							"Aug 2023 - Dec 2024 (1 yr 5 mos)",
							["Python", "FastAPI", "Docker", "MySQL", "Pytest", "JavaScript", "Quart"],
							"experience-card-necc",
						),
						card(
							MARTIAN_CONTENT,
							"Software Engineer at ",
							"Martian",
							"https://withmartian.com",
							"Apr 2024 - Jul 2024 (4 mos)",
							["Python", "FastAPI", "Litestar", "Docker", "Pytest", "Jinja", "MongoDB"],
							"experience-card-martian",
						),
						card(
							["Designing, creating, and maintaining a backend service to integrate load boards across North America."],
							"Backend Software Engineer at ",
							"Shipwell",
							"https://shipwell.com",
							"Sep 2022 - Jul 2023 (11 mos)",
							["Python", "FastAPI", "Docker", "PostgreSQL", "FastAPI", "Pytest", "SQLAlchemy", "AWS", "RabbitMQ", "Redis"],
							"experience-card-shipwell",
						),
						card(
							PINTEREST_CONTENT,
							"Software Engineer at ",
							"Pinterest",
							"https://pinterest.com",
							"Sep 2019 - Jul 2022 (2 yrs 11 mos)",
							["Python", "SQL", "Flask", "Docker", "AWS", "React.JS", "Pytest", "Pandas"],
							"experience-card-pinterest",
						),
						card(
							["We created screening processes for new employees, and we also helped some colleagues with mentorships. I interviewed many candidates to be Python-focused software engineers."],
							"Software Engineer at ",
							"BairesDev",
							"https://bairesdev.com",
							"Sep 2019 - Jul 2022 (2 yrs 11 mos)",
							["Python"],
							"experience-card-bairesdev",
						),
						card(
							["I ministered the following subjects: • Algorithms and Data Structures. • Relational Database. • Multi and Hypermedia Systems. • Algorithm Analysis and Graph Theory. • Object-Oriented Programming."],
							"Assistant Professor at ",
							"State University of Maringá",
							"https://www.uem.br",
							"Apr 2019 - Oct 2019 (7 mos)",
							["Python", "SQL", "C", "Java"],
							"experience-card-uem",
						),
						card(
							SEEBOT_CONTENT,
							"Software Engineer at ",
							"Seebot",
							"https://www.seebot.com.br",
							"Oct 2015 - Sep 2019 (3 yrs 11 mos)",
							["Python", "Gevent", "Linux", "Graph Theory", "Systemd"],
							"experience-card-seebot",
						),
						card(
							EARLYSEC_CONTENT,
							"Data Scientist at ",
							"EarlySec",
							None,
							"Jun 2018 - Mar 2019 (10 mos)",
							["Python", "Java", "Natural Language Processing", "Elasticsearch", "Kafka", "Pytest"],
						),
						cols_lg=2,
						cols_xl=2,
					),
					Div(H3("Projects", cls=TextT.primary), id="projects"),
					Grid(
						Card(
							"Website that aggregates events from different websites and shows them in a single place.",
							header=A(
								CardTitle("akingressos.com.br (PT-BR)"),
								href="https://akingressos.com.br",
							),
						),
					),
					Div(H3("Education", cls=TextT.primary), id="education"),
					Grid(
						card(
							MASTERS_CONTENT,
							"Master's Degree in Computer Science at ",
							"State University of Maringá",
							"https://www.uem.br",
							"2014 - 2016 (2 yrs)",
							["Python", "Graph Theory"],
						),
						card(
							GRADUATION_CONTENT,
							"Bachelor's Degree in Computer Science at ",
							"State University of Maringá",
							"https://www.uem.br",
							"2010 - 2013 (4 yrs)",
							["Python", "Graph Theory"],
						),
					),
					Div(H3("Scientific Papers", cls=TextT.primary), id="scientific-papers"),
					Grid(
						card(
							PAPER_1,
							"",
							"Journal of Universal Computer Science",
							"https://www.jucs.org/jucs_23_5/solving_a_large_real/",
							"May 2017",
							[],
						),
						card(
							PAPER_2,
							"",
							"XLVIII SBPO - Simpósio Brasileiro de Pesquisa Operacional (PT-BR)",
							"http://www.din.uem.br/sbpo/sbpo2016/pdf/156702.pdf",
							"Sep 2016",
							[],
						),
					),
				),
			),
			DividerLine(),
			Footer(
				"Built with ",
				A("FastHTML", href="https://www.fastht.ml", cls=AT.primary),
				" and ",
				A("MonsterUI", href="https://monsterui.answer.ai/", cls=AT.primary),
			),
		),
	)