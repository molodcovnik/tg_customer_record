import os
from dotenv import load_dotenv
import logging


# Configure dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


# Configure logging
#logging.basicConfig(filename='info.log', level=logging.INFO)


# Environments
token = os.getenv('TOKEN')
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')
port = os.getenv('port')



