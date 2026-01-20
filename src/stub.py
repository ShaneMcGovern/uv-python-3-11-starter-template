"""Simple logging example using module-level functions."""

import logging
from sys import stderr

logging.basicConfig(level=logging.INFO, stream=stderr)

logger = logging.getLogger(__name__)


def message() -> None:
    """Log a license reminder message."""
    logger.info("Don't forget to read the LICENSE file.")


def main() -> None:
    """Entry point for the application."""
    message()


if __name__ == "__main__":
    main()
