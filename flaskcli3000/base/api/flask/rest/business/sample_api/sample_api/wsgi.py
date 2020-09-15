 
import os
from dotenv import load_dotenv, find_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(find_dotenv())

from .app import create_app  # noqa

app = create_app()

if __name__ == "__main__":
    app.run()