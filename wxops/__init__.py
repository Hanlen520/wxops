import json
from config import ENTRY_CONFIG


with open(ENTRY_CONFIG) as f:
    APP_DICT = json.load(f)['app']
