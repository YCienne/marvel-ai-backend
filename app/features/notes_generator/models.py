from pydantic import BaseModel

class NotesGeneratorInput(BaseModel):
    input_text: str
    output_format: str
