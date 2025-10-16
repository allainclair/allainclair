from markdown_it import MarkdownIt
from markdown_it.token import Token
from markdown_it.renderer import RendererHTML
from markdown_it.common.utils import escapeHtml
from mdit_py_plugins.anchors import anchors_plugin
from fasthtml.common import Div, NotStr

HEADING_CLASSES = {
	"h1": "text-4xl font-bold text-primary mb-4",
	"h2": "text-2xl font-bold text-primary mb-3",
	"h3": "text-xl font-semibold text-primary mt-3 mb-2",
	"h4": "text-lg font-semibold mt-3 mb-2",
	"h5": "text-md font-semibold mt-2 mb-1",
	"h6": "text-md font-semibold mt-2 mb-1",
}


class DaisyUIRenderer(RendererHTML):
	"""Custom renderer that outputs HTML with daisyUI classes"""

	def __init__(self):
		super().__init__()

	def heading_open(self, tokens: list[Token], idx: int, options, env):
		token = tokens[idx]
		id_attr = self.renderAttrs(token)
		h_level = HEADING_CLASSES[token.tag]
		return f'<{token.tag} class="{h_level}"{id_attr}>'

	def paragraph_open(self, tokens, idx, options, env):
		return '<p class="mt-2 leading-relaxed">'

	def fence(self, tokens, idx, options, env):
		token = tokens[idx]
		lang = token.info or ''
		code = token.content

		# Return as daisyUI mockup-code
		lines = code.rstrip('\n').split('\n')
		code_lines = []
		for i, line in enumerate(lines, 1):
			escaped = escapeHtml(line) if line else ""
			code_lines.append(f'  <pre data-prefix="{i}"><code>{escaped}</code></pre>')

		return f'<div class="mockup-code w-full mt-4">\n' + '\n'.join(code_lines) + '\n</div>'

	def link_open(self, tokens, idx, options, env):
		token = tokens[idx]
		href = token.attrGet('href') or ''
		return f'<a href="{href}" class="link link-primary link-hover">'

	def bullet_list_open(self, tokens, idx, options, env):
		return '<ul class="list-disc list-outside ml-5 mt-2 space-y-1">'

	# def ordered_list_open(self, tokens, idx, options, env):
	# 	return '<ol class="list-decimal list-inside mt-2 space-y-1">'

	def blockquote_open(self, tokens, idx, options, env):
		return '<div class="border-l-4 border-primary pl-4 italic my-4 bg-base-200 py-2">'

	def blockquote_close(self, tokens, idx, options, env):
		return '</div>'

	def table_open(self, tokens, idx, options, env):
		return '<table class="table table-zebra w-full mt-4">'

	def strong_open(self, tokens, idx, options, env):
		return '<strong class="font-bold">'


def create_markdown_parser():
	"""Create configured Markdown parser with plugins"""
	md = (
		MarkdownIt('commonmark', {'html': True, 'breaks': False, 'linkify': True})
		.use(
			anchors_plugin,
			max_level=3,
			#slug_func=custom_slug,
			#permalink=True,
			#permalinkSymbol="¶",
			#permalinkBefore=False,
		)  # For automatic ID generation from heading text
		.enable(['table', 'strikethrough'])
	)

	md.renderer = DaisyUIRenderer()
	return md


# Create a shared parser instance
_parser = create_markdown_parser()


def md_to_html(md_content: str) -> str:
	"""
	Convert Markdown to HTML with daisyUI classes

	Returns:
		str: HTML content
	"""
	html = _parser.render(md_content)
	return html


def md_to_fasthtml(md_content: str):
	"""
	Convert markdown to FastHTML component

	Args:
		md_content: Markdown string content

	Returns:
		FastHTML Div component with rendered HTML
	"""
	html = md_to_html(md_content)
	return Div(NotStr(html))
