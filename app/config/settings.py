from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# ==========================
# Assistant Configuration
# ==========================

ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Jarvis")

# ==========================
# API Keys
# ==========================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ==========================
# Default AI Provider
# ==========================

DEFAULT_PROVIDER = os.getenv("DEFAULT_PROVIDER", "groq").lower()

SUPPORTED_PROVIDERS = [
    "groq",
    "openai"
]