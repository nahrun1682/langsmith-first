import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

model_name = 'gpt-3.5-turbo-16k'
project_name = 'langsmith_first'