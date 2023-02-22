"""Main Module."""
import logging
from incolume.py.prospect.openai_api import chat_connect as cc


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
           "%(module)s;%(funcName)s;%(message)s",
)


def run():
    """Run main module."""
    logging.debug('starting ..')
    print(cc.TOKEN)


if __name__ == "__main__":
    run()
