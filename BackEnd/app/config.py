import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR,'..','.env'))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_STRING')
    SQLALCHEMY_TRACK_MODIFICATIONS = False