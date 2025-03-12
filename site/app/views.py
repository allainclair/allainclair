from monsterui.all import AT, H2, H3, H5, UkIcon, Grid, UkIconLink, CardFooter, DivHStacked, FlexT, DivRAligned, DivLAligned, Card, CardT, CardTitle, DivFullySpaced, Label
from fasthtml.common import Title, A, Div, Main, Link, Ul, Li, Span, FT


def card(
	body_contents: list[FT],  # Can't type this
	title_text: str,
	title_link_text: str,
	title_link_href: str | None,
	period: str,
	techs: list[str],
	cls: str | None = None
) -> Card:
	if title_link_href:
		card_title = CardTitle(
			title_text,
			A(title_link_text, href=title_link_href or True, cls=AT.text),
		)
	else:
		card_title = CardTitle(f"{title_text}{title_link_text}")
	if techs:
		tech_elements = DivHStacked(
			Div("Techs: "),
			*[Div(Label(tech)) for tech in techs],
			cls=(FlexT.wrap, "space-x-2"),
		),
	else:
		tech_elements = None

	return Card(
		DivLAligned(
			Div(UkIcon("calendar")),
			Div(period),
			cls="space-x-2"

		),
		*body_contents,
		tech_elements,
		header=card_title,
		cls=cls or None,
	),

def accordion(title: str, content_elements: list[FT | str]) -> Ul:
	return Ul(
		Li(
			A(
				Span(title),
				Span(
					UkIcon("chevron-down"),
					cls="uk-accordion-icon size-4"
				),
				href=True,
				cls="uk-accordion-title",
			),
			Div(
				*content_elements,
				cls="uk-accordion-content",
			),
		),
		data_uk_accordion=True,
		style="margin-top: 0",  # CSS class not working.
	)