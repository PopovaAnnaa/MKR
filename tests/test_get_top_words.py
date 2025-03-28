import pytest
import os
from main import get_top_words 

@pytest.fixture
def setup_files():
    input_filename = 'test_input.txt'
    output_filename = 'test_output.txt'
    yield input_filename, output_filename

    if os.path.exists(input_filename):
        os.remove(input_filename)
    if os.path.exists(output_filename):
        os.remove(output_filename)

@pytest.mark.parametrize("input_text, top_n, expected_output", [
    ("cat dog rabbit cat cat rabbit cat dog", 3, ['cat-4', 'dog-2', 'rabbit-2']),
    ("sun moon star", 5, ['sun-1', 'moon-1', 'star-1']),
    ("", 3, []),  
])

def test_get_top_words(setup_files, input_text, top_n, expected_output):
    input_filename, output_filename = setup_files
    
    with open(input_filename, 'w', encoding='utf-8') as f:
        f.write(input_text)
    
    get_top_words(input_filename, output_filename, top_n)
    
    with open(output_filename, 'r', encoding='utf-8') as f:
        output = f.read().strip().split('\n')
    
    if output == ['']:
        output = []
    
    assert output == expected_output, f"Expected {expected_output}, but got {output}"
