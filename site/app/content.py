from app.views import accordion
from fasthtml.common import A, P, Div
from app.i18n import i18n

def get_telnyx_content(user_language: str) -> list[str]:
	return [
		Div(i18n("• Enabled our customers to monitor and manage thousands of messages daily.", user_language)),
		Div(i18n("• Worked on about 8 microservices, designing, developing, and maintaining about 24 HTTP endpoints.", user_language)),
	]

def get_necc_content(user_language: str):
	return [accordion(
		i18n("• Designed and maintained education-tech apps, adding and improving features to make teachers and students have modern and faster apps: improved page load by 200%.", user_language),
		[i18n("• Worked on migrating one Java monolith app, breaking it into some Python microservices.", user_language)],
	)]

def get_martian_content(user_language: str):
	martian_a_gh_adapters = A("github.com/withmartian/llm-adapters", href="https://github.com/withmartian/llm-adapters/commits/main/?author=allainclair", cls="link", target="_blank")
	return [
		i18n("• Built Large Language Models (LLM) adapters enabling seamless integration with 12+ proprietary and open-source models. See open source repository: ", user_language),
		martian_a_gh_adapters,
		Div(i18n("• Developed a Sales Dashboard (front and backend) to give the Sales Team insights into our customers.", user_language)),
	]

def get_pinterest_content(user_language: str):
	return [
		P(i18n("• Built and maintained internal Trust & Safety tools used by 100+ moderators daily, supporting them to reduce inappropriate content.", user_language)),
		P(
			i18n(
			"• Designed time-series monitoring dashboards for Ads systems, improving observability and reducing downtime.",
			user_language,
			),
		),
		P(
			i18n("• Conducted 340+ technical interviews for Python engineers and mentored junior developers.",
			 user_language,
			)
		)
	]

def get_seebot_content(user_language: str):
	return [
		P(
			i18n(
				"• Assembled an entire Smart Traffic Light (STL) that can sense streets using cameras and act (open/close) autonomously. Main achievements were: led 5 software engineers, created an STL hardware and software controllers, traffic simulators for traffic optimization, and web dashboards.",
				user_language,
			),
		),
		P(i18n(
			"• Created a traffic simulator using SUMO (Simulation of Urban MObility). My main algorithm on this simulator had 200% to 400% waiting time optimization on light to medium vehicle traffic.",
			user_language
		)),
		P(
			i18n(
				"• Deployed our smart traffic light in 4 real crossing roads. To achieve this, I had to: do research in the traffic optimization area by using smart traffic lights, design and develop optimization algorithms for STLs, design and create embedded distributed real-time systems for the STL with a microservice architecture.",
				user_language,
			),
		),
	]

def get_earlysec_content(user_language: str):
	return [
		P(i18n(
			"• Created security apps to advise our clients on assurance issues by using Natural Language Processing (NLP) techniques to filter, train, classify, and cluster social media messages. This way, we could alert our clients if something unusual was happening.",
			user_language)),
	]

def get_masters_content(user_language: str):
	return [
		accordion(
			i18n("Major in Combinatorial Optimization, Bus Driver Schedule Problem", user_language),
			[i18n("Algorithms based on Variable Neighborhood Search (VNS) metaheuristic applied in the Bus Driver Schedule Problem.", user_language)],
		)
	]

def get_graduation_content(user_language: str):
	return [
		accordion(
			i18n("Major in Computer Science, Combinatorial Optimization, Feedback Arc Set Problem", user_language),
			[i18n("A genetic algorithm for the Feedback Arc Set Problem.", user_language)],
		)
	]

def get_paper_1(user_language: str):
	return [i18n("Solving a Large Real-world Bus Driver Scheduling Problem with a Multi-assignment based Heuristic Algorithm.", user_language)]

# Keep PAPER_2 as is since it's already in Portuguese
PAPER_2 = ["Algoritmos baseados na meta-heurística VNS aplicados ao Problema de Escalonamento de Motoristas de Ônibus"]