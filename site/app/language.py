from starlette.requests import Request


def get_user_language(req: Request, user_language: str | None) -> str:
	"""Determine the user's language preference.

	Checks the provided user_language cookie first. If not provided, it checks the
	"Accept-Language" header from the request. Defaults to 'en' if no preference
	is found.
	"""
	if user_language is not None:
		return user_language

	if not req.headers["Accept-Language"]:
		return "en"

	languages = [lang.split(';')[0].strip() for lang in req.headers["Accept-Language"].split(',')]
	for lang in languages:
		if "pt" in lang.lower():
			return "pt"
		if "en" in lang.lower():
			return "en"

	return "en"
