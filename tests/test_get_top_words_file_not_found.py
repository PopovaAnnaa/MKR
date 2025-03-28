from main import get_top_words 

def test_get_top_words_file_not_found():
    input_filename = 'non_existent_input.txt'
    output_filename = 'test_output.txt'
    
    get_top_words(input_filename, output_filename)
