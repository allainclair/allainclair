from fasthtml import APIRouter
from starlette.requests import Request
from fasthtml.common import (
	Div,
	Span,
	Figure,
	Img,
	H2,
	A,
	Header,
	cookie,
	Ul,
	Li,
	Title,
	Body,
)
from app.blog.loader import get_blog_post, render_blog_post_content
from datetime import datetime, UTC
from timeago import format

from app.language import get_user_language
from app.views import button_translate, header
from app.i18n import i18n

router = APIRouter()

CODE_STR_COLOR = "text-success"
CODE_KEYWORD_COLOR = "text-warning"
CODE_BUILT_IN_COLOR = "text-primary"
CODE_BASE_COLOR = "text-base-content"
CODE_FUNCTION_COLOR = "text-accent"
CODE_BASE_COLOR_50 = "text-base-content/50"


@router("/blog")
async def blog(
	req: Request,
	user_language: str | None = None,
):
	user_language = get_user_language(req, user_language)

	body_content = await _body_content(
		user_language,
	),
	return (
		Title("Allainclair Flausino dos Santos"),
		Body(
			*body_content,
			id="body-content",
		),
	), cookie("user_language", user_language)


@router("/blog/main-content")
async def blog(user_language: str):
	blog_contents = [await blog_content_1(user_language)]
	return (
		_main_content(blog_contents),
		button_translate(user_language, "/blog/body-content", "true"),
	)


@router("/blog/body-content")  # type: ignore[misc]
async def get(language: str):  # type: ignore[no-untyped-def]  # noqa: ANN201
	return await _body_content(language), cookie("user_language", language)


@router("/blog/mastering-async-io-in-python/body-content")  # type: ignore[misc]
async def get(language: str):  # type: ignore[no-untyped-def]  # noqa: ANN201
	return (
		await _body_content(
			language,
			"/blog/mastering-async-io-in-python/body-content",
			i18n("Mastering Async IO in Python", language),
			"/blog/mastering-async-io-in-python",
		),
		cookie("user_language", language),
	)


@router("/blog/mastering-async-io-in-python")  # type: ignore[misc]
async def get(
	req: Request,
	user_language: str | None = None,
):  # type: ignore[no-untyped-def]  # noqa: ANN201
	user_language = get_user_language(req, user_language)

	body_content = await _body_content(
		user_language,
		"/blog/mastering-async-io-in-python/body-content",
		i18n("Mastering Async IO in Python", user_language),
		"/blog/mastering-async-io-in-python"
	),
	return (
		Title("Allainclair Flausino dos Santos"),
		Body(
			*body_content,
			id="body-content",
		),
	), cookie("user_language", user_language)


@router("/blog/mastering-async-io-in-python/main-content")  # type: ignore[misc]
async def get(user_language: str):  # type: ignore[no-untyped-def]  # noqa: ANN201
	blog_contents = [await blog_content_1(user_language)]
	return (
		_main_content(
			blog_contents,
			i18n("Mastering Async IO in Python", user_language),
			"/blog/mastering-async-io-in-python",
		),
		button_translate(
			user_language,
			"/blog/mastering-async-io-in-python/body-content",
			"true",
		),
	)


async def _body_content(
	user_language: str,
	path_translate: str = "/blog/body-content",
	breadcrumbs_li_name: str | None = None,
	breadcrumbs_li_path: str | None = None,
) -> tuple[Header, Div]:
	blog_contents = [await blog_content_1(user_language)]
	return (
		header(user_language, path_translate, "blog"),
		_main_content(blog_contents, breadcrumbs_li_name, breadcrumbs_li_path),
	)


def _main_content(
	blog_contents: list[Div],
	breadcrumbs_li_name: str | None = None,
	breadcrumbs_li_path: str | None = None,
) -> Div:
	return Div(
		_blog_breadcrumbs(breadcrumbs_li_name, breadcrumbs_li_path),
		*blog_contents,
		id="main-content",
		cls="container mx-auto gap-4 mt-4 w-11/12",
	)


async def blog_content_1(user_language: str) -> Div:
	created_at = datetime(2025, 10, 16, 0, 0, 0, tzinfo=UTC)
	created_at_str_date = created_at.strftime("%Y-%m-%d %H:%M:%S %Z")
	now = datetime.now(UTC)
	if user_language == "pt":
		html_content = await get_blog_post(
			"app/content/blog/2025-10-09-async-python-pt.md"
		)
		published = format(created_at, now, "pt_BR")

	else:
		html_content = await get_blog_post(
			"app/content/blog/2025-10-09-async-python-en.md"
		)
		published = format(created_at, now)


	return Div(
		Figure(
			Img(
				src="/app/images/async.jpg",
				alt="Async banner",
				cls="object-cover object-center",
			),
			cls="h-24",
		),
		Div(
			Span(
				i18n("Published ", user_language),
				f"{published} ",
				i18n("by Allainclair", user_language),
				data_tip=f"{created_at_str_date}",
				cls="tooltip tooltip-right text-base-content/60 inline-block w-fit",
			),
			# Render the blog post content from markdown
			render_blog_post_content(html_content),
			cls="card-body",
		),
		cls="card bg-base-300 shadow-md mt-4",
	)


def _blog_breadcrumbs(name: str | None = None, path: str | None = None) -> Div:
	li = None
	if name and path:
		li = Li(
			A(
				H2(name, cls="text-2xl font-bold"),
				href=path,
				cls="text-primary",
			),
		)
	return Div(
		Ul(
			Li(
				A(
					H2("Blog", cls="text-2xl font-bold"),
					href="/blog",
					cls="text-primary",
				),
			),
			li,
		),
		id="blog-breadcrumbs",
		cls="breadcrumbs",
	)
