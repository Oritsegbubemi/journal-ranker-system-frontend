# import os
# import json

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# CONFIG_FILE = os.path.join(BASE_DIR, 'journals/config.json')

# try:
#     with open(CONFIG_FILE) as config_file:
#         config = json.load(config_file)
#         if (config['PROD'] == "True"):
#             from .prod import *
#         else:
#             from .dev import *

# except:
#     from .dev import *