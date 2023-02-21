import openai
import dotenv
import os
import logging


__author__ = "@britodfbr"  # pragma: no cover


dotenv.load_dotenv()
TOKEN = os.environ.get('OPENAI_KEY')

logging.debug(TOKEN)

