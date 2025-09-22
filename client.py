import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the API key from the environment
API_KEY = os.getenv("GENAI_API_KEY")

# Initialize the Gemini AI client
client = genai.Client(api_key=API_KEY)

# Function to process commands via AI
def aiProcess(command: str) -> str:
    """
    Send a command to Gemini AI and return the response.
    """
    completion = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Nova skilled in general tasks like Alexa and Google Cloud"},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content
