import os
from dotenv import load_dotenv

def load_env(env_path: str):
    if not os.path.exists(env_path):
        raise FileNotFoundError(f".env file not found at: {env_path}")

    load_dotenv(env_path)