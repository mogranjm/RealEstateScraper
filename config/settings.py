import os.path
from pathlib import Path

from dotenv import dotenv_values

BASE_DIR = Path(__file__).parent.parent
ENV_DIR = BASE_DIR / '.env'
env = dotenv_values(ENV_DIR)

if __name__ == "__main__":
	assert os.path.exists(BASE_DIR)
	print(env)