from collections import Counter
import re

def get_top_words(input_file, output_file, top_n=10):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read().lower()

        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words).most_common(top_n)

        with open(output_file, 'w', encoding='utf-8') as file:
            for word, count in word_counts:
                file.write(f"{word}-{count}\n")
        
        print(f"Результати збережено в {output_file}")
    except FileNotFoundError:
        print("Файл не знайдено!")
    except Exception as e:
        print(f"Помилка: {e}")


input_filename = "input.txt"  
output_filename = "output.txt"
get_top_words(input_filename, output_filename)
