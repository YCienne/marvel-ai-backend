# app/features/notes_generator/core.py

import logging
from typing import Dict, Any
from app.features.notes_generator.tools import generate_notes_tool

logger = logging.getLogger(__name__)

def executor_function(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executor function to generate structured notes based on input data.

    Parameters:
    - data (dict): Contains 'input_text' (str) and 'output_format' (str).
    
    Returns:
    - dict: Contains generated 'notes' in the specified 'output_format'.
    """
    try:
        input_text = data.get("input_text")
        output_format = data.get("output_format")

        if not input_text or not output_format:
            raise ValueError("Missing required fields: 'input_text' and 'output_format'")

        
        result = generate_notes_tool.invoke({
            "input_text": input_text,
            "output_format": output_format
        })

        logger.info(f"Generated notes: {result}")

        return {
            "notes": result,
            "format": output_format
        }

    except Exception as e:
        logger.error(f"Error in executor_function: {e}")
        raise ValueError(f"Failed to generate notes: {str(e)}")
