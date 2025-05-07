import os
from dotenv import load_dotenv
from google.auth import default
from google.auth.transport.requests import Request
from google.auth.exceptions import DefaultCredentialsError
from vertexai.preview.language_models import TextGenerationModel
from vertexai import init
from langchain.tools import tool
from app.features.notes_generator.models import NotesGeneratorInput

# Load environment variables
load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION", "us-central1")

if not PROJECT_ID:
    raise ValueError("PROJECT_ID must be set in the environment variables.")

# Google Cloud Authentication 
try:
    credentials, project = default()
    credentials.refresh(Request()) 
    print(f"Authenticated with project: {project}")
except DefaultCredentialsError as e:
    print(f"Authentication failed: {str(e)}")
    raise e 

# Initialize Vertex AI
init(project=PROJECT_ID, location=LOCATION)

# Core function to generate notes
def _generate_notes(input_text: str, output_format: str) -> str:
    try:
        # text generation model 
        model = TextGenerationModel.from_pretrained("gemini-pro")

        prompt = f"Generate structured notes in {output_format} format for the following text:\n\n{input_text}"

        response = model.predict(
            prompt=prompt,
            temperature=0.7,
            max_output_tokens=1024,
        )

        return response.text
    except Exception as e:
        raise ValueError(f"Error in _generate_notes: {str(e)}")


# LangChain-compatible tool
@tool("generate_structured_notes", return_direct=True)
def generate_notes_tool(input_text: str, output_format: str = "bullet points") -> str:
    """
    Generates structured notes using Vertex AI based on input text and desired format.
    
    Parameters:
    - input_text: Raw text to process
    - output_format: Format of notes (e.g., bullet points, paragraph, table)

    Returns:
    - str: Structured notes
    """
    return _generate_notes(input_text, output_format)
