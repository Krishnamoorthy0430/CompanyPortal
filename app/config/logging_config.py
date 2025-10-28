import logging


def setup_logging(level: str = "INFO") -> None:
	"""Configure basic logging for the application.

	This keeps logging simple and suitable for local development.
	"""
	logging.basicConfig(
		level=getattr(logging, level.upper(), logging.INFO),
		format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
	)

	# Optionally reduce log level for noisy libraries
	logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
	logging.getLogger("uvicorn.error").setLevel(logging.WARNING)

