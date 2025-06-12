from google import genai
from config import GEMINI_API_KEY

# Initialize Gemini client
def run_analysis(prompt: str):
   client = genai.Client(api_key=GEMINI_API_KEY)

   response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt
    )
   return response.text
