from app.features.notes_generator.core import executor_function
from app.features.notes_generator.models import NotesGeneratorInput
import pytest

# Test case for normal operation
def test_notes_generation_valid_input():
    data = {
        "input_text": "Python is a popular programming language.",
        "output_format": "bullet"
    }
    result = executor_function(data)
    assert "notes" in result
    assert "format" in result
    assert result['format'] == "bullet"

# Test case for missing input_text
def test_notes_generation_missing_input_text():
    with pytest.raises(ValueError):
        data = NotesGeneratorInput(output_format="bullet")  
        executor_function(data)

# Test case for missing output_format
def test_notes_generation_missing_output_format():
    with pytest.raises(ValueError):
        data = NotesGeneratorInput(input_text="Python is a popular programming language.")  
        executor_function(data)

# Test case for invalid output_format
def test_notes_generation_invalid_output_format():
    data = NotesGeneratorInput(
        input_text="Python is a popular programming language.",
        output_format="invalid_format"
    )
    with pytest.raises(ValueError):
        executor_function(data)
