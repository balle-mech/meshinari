import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# 認証に必要なキーとトークン
HOT_PEPPER_API_KEY = os.environ.get('HOT_PEPPER_API_KEY')
GEOCODING_API_KEY = os.environ.get('GEOCODING_API_KEY')
