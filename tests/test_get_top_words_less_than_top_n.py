import os
from main import get_top_words 

def test_get_top_words_less_than_top_n():
    input_filename = 'test_input.txt'
    output_filename = 'test_output.txt'

    with open(input_filename, 'w', encoding='utf-8') as f:
        f.write("apple orange banana")

    get_top_words(input_filename, output_filename, top_n=5)
    
    with open(output_filename, 'r', encoding='utf-8') as f:
        output = f.read().strip().split('\n')
    
    expected = ['apple-1', 'orange-1', 'banana-1']
    
    assert output == expected, f"Expected {expected}, but got {output}"
    
    os.remove(input_filename)
    os.remove(output_filename)
