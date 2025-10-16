from fasthtml.common import A, H2, H3, Div, Header, Ul, Li, Button
from app.icons import language, envelope, linkedin, github, user_tie, laptop_code, graduation_cap, newspaper, blog, whatsapp, file_user
from app.i18n import i18n


def button_translate(user_language: str, path_translate: str, hx_swap_oob: str | None = None)-> Button:
	if user_language == "en":
		language_arg = "pt"
		text = "pt-BR"
		data_tip = "Traduzir para Português"
	else:
		language_arg = "en"
		text = "en"
		data_tip = "Translate to English"

	return Button(
		language(),
		text,
		cls="btn btn-soft btn-info btn-sm tooltip tooltip-left",
		data_tip=data_tip,
		id="button-translate",
		hx_get=f"{path_translate}?language={language_arg}",
		hx_target="#body-content",
		hx_swap_oob=hx_swap_oob,
	)


def header(user_language: str, path_translate: str, tab_active: str = "professional-experience") -> Header:
	button_lang = button_translate(user_language, path_translate)
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
					#cls="link",
				),
				cls="flex justify-center gap-2",
			),

			Div(
				tablist_content(user_language, tab_active),
				cls="flex justify-center",
			),

			cls="container mx-auto mt-4 w-11/12",
		),
	)


def tablist_content(user_language: str, tab_active: str) -> Div:
	return Div(
		A(
			user_tie(),
			Div(i18n("Professional Experience", user_language), cls="ml-2"),
			role="tab",
			href="/?tab_active=professional-experience#professional-experience",
			cls="tab tab-active" if tab_active == "professional-experience" else "tab",
			onclick="document.querySelectorAll('.tab').forEach(t => t.classList.remove('tab-active')); this.classList.add('tab-active')",
		),
		A(
			laptop_code(),
			Div(i18n("Projects", user_language), cls="ml-2"),
			role="tab",
			href="/?tab_active=projects#projects",
			cls="tab tab-active" if tab_active == "projects" else "tab",
			onclick="document.querySelectorAll('.tab').forEach(t => t.classList.remove('tab-active')); this.classList.add('tab-active')",
		),
		A(
			graduation_cap(),
			Div(i18n("Education", user_language), cls="ml-2"),
			role="tab",
			href="/?tab_active=education#education",
			cls="tab tab-active" if tab_active == "education" else "tab",
			onclick="document.querySelectorAll('.tab').forEach(t => t.classList.remove('tab-active')); this.classList.add('tab-active')",
		),
		A(
			newspaper(),
			Div(i18n("Scientific Papers", user_language), cls="ml-2"),
			role="tab",
			href="/?tab_active=scientific-papers#scientific-papers",
			cls="tab tab-active" if tab_active == "scientific-papers" else "tab",
			onclick="document.querySelectorAll('.tab').forEach(t => t.classList.remove('tab-active')); this.classList.add('tab-active')",
		),
		A(
			blog(),
			Div("Blog", cls="ml-2"),
			id="tab-blog",
			role="tab",
			hx_get="/blog/main-content",
			hx_target="#main-content",
			hx_swap="outerHTML",
			hx_push_url="/blog",
			cls="tab tab-active" if tab_active == "blog" else "tab",
			onclick="document.querySelectorAll('.tab').forEach(t => t.classList.remove('tab-active')); this.classList.add('tab-active')",
		),
		id="tablist-content",
		role="tablist",
		cls="tabs tabs-box justify-center my-2",
	)
