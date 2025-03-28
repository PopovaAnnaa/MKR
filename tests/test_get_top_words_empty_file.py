import os
from main import get_top_words 

def test_get_top_words_empty_file():
    input_filename = 'empty_input.txt'
    output_filename = 'test_output.txt'

    with open(input_filename, 'w', encoding='utf-8') as f:
        pass
    
    get_top_words(input_filename, output_filename)
    
    with open(output_filename, 'r', encoding='utf-8') as f:
        output = f.read().strip()
    
    assert output == '', f"Expected empty output, but got {output}"
    
    os.remove(input_filename)
    os.remove(output_filename)
