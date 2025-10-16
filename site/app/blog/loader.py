import aiofiles
from fasthtml.common import Div, NotStr
from app.markdown_converter import md_to_html


async def get_blog_post(path: str) -> str:
	"""
	Get a single blog post content by path

	Args:
		path: The file path (e.g., 'app/blog/2025-10-09-async-python-full.md')

	Returns:
		HTML content string or empty string if not found
	"""
	try:
		async with aiofiles.open(path) as f:
			content = await f.read()
		html = md_to_html(content)
		return html
	except FileNotFoundError:
		return ""


def render_blog_post_content(html_content: str) -> Div:
	"""
	Render blog post content as FastHTML

	Args:
		html_content: HTML string content

	Returns:
		FastHTML Div with post content
	"""
	return Div(NotStr(html_content))
