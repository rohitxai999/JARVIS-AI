import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("ELEVENLABS_API_KEY")

if key:
    print("API KEY FOUND")
else:
    print("API KEY NOT FOUND")