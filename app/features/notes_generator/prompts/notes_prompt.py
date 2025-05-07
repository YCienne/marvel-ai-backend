# app/features/notes_generator/prompts/base_prompts.py

from langchain.prompts import PromptTemplate

# Define a prompt template for generating notes
def get_notes_prompt() -> PromptTemplate:
    return PromptTemplate(
        input_variables=["input_text", "output_format"],
        template="""
        You are a helpful assistant that generates structured notes from raw input text.
        
        Input Text: {input_text}
        
        The notes should be in the following format: {output_format}. 
        Make sure the notes are concise, accurate, and easy to understand.

        Output: 
        """
    )
