from app.views import accordion
from fasthtml.common import A, P

TELNYX_CONTENT = ["I have been developing backend web APIs for SMS messaging management."]

NECC_CONTENT = [accordion(
	"We designed, created, and maintained ed-tech apps.",
	["I worked on creating Python FastAPI/Quart/JavaScript apps with MySQL to manage data."],
)]

MARTIAN_A_GH_ADAPTERS = A("(github.com/withmartian/adapters)", href="https://github.com/withmartian/adapters", cls="link", target="_blank")
MARTIAN_CONTENT = [
	"The main Martian feature is an LLM router: a user can send a prompt, and the Martian’s model will decide on the best LLM for it. I contributed to ",
	MARTIAN_A_GH_ADAPTERS,
	". It interfaces with a large set of open and proprietary Large Language Models (LLMs). I  developed a Sales Dashboard (front and backend) to give the Sales Team insights into our customers. This dashboard used HTMX/Jinja for frontend and Litestar, Pydantic, MongoDB for the backend.",
]

PINTEREST_CONTENT = [
	P("Trust and Safety Tools Team: we provided tools to keep Pinterest trust and safe. We developed and maintained web tools to assist agents in fast-track trust and safety issues and solve them."),
	P("Ads interface and Growth Team: we provided monitoring and alerting tools to improve observability on Ads Interface & Growth systems. We worked and developed time-series dashboards for monitoring, alerting and reporting, Google Chrome extension to check API requests miss behavior."),
]

SEEBOT_CONTENT = [
	P("We assembled an entire smart traffic light (STL) that can sense streets using cameras and act (open/close) autonomously: when I led software engineers, we created a STL hardware and software controllers, traffic simulators for traffic optimization, and dashboards."),
	P("We created a traffic simulator using SUMO (Simulation of Urban MObility): our main algorithm on this simulator had 200% to 400% waiting time optimization on light to medium vehicle traffic. We also deployed our STL in four real crossing roads. To achieve this, we had to do researches in traffic optimization area by using smart traffic lights, design and develop optimization algorithms for smart traffic lights, design and create an embedded distributed real-time systems for the STL with a microservice architecture."),
]

EARLYSEC_CONTENT = [
	P("We created security systems to advise our clients on assurance issues: we used Natural Language Processing (NLP) techniques to filter, train, classify, and cluster social media messages. This way, we could alert our clients if something unusual was happening."),
]

MASTERS_CONTENT = [
	accordion(
		"Major in Combinatorial Optimization, Bus Driver Schedule Problem",
		["Algorithms based on Variable Neighborhood Search (VNS) metaheuristic applied in the Bus Driver Schedule Problem."],
	)
]

GRADUATION_CONTENT = [
	accordion(
		"Major in Computer Science, Combinatorial Optimization, Feedback Arc Set Problem",
		["A genetic algorithm for the Feedback Arc Set Problem."],
	)
]

PAPER_1 = ["Solving a Large Real-world Bus Driver Scheduling Problem with a Multi-assignment based Heuristic Algorithm."]
PAPER_2 = ["Algoritmos baseados na meta-heurística VNS aplicados ao Problema de Escalonamento de Motoristas de Ônibus"]