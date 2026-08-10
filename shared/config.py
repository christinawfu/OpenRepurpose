import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DISGENET_API_KEY = os.getenv("DISGENET_API_KEY")
OMIM_API_KEY = os.getenv("OMIM_API_KEY")