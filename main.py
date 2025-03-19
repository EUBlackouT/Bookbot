import sys
if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
from stats import count_words 
from stats import count_characters
from stats import sorted_characters

def get_book_text(filepath):
    with open(sys.argv[1]) as f:
        file_content = f.read()
    return(file_content)


def main():
     filepath = sys.argv[1]
        
     book_text = get_book_text(filepath)
     word_count = count_words(book_text)
     char_count = count_characters(book_text)
     sorted_count = sorted_characters(char_count)

      
     print("============ BOOKBOT ============")
     print(f"Analyzing book found at {filepath}...")
     print("----------- Word Count ----------")
     print(f"Found {word_count} total words")
     print("--------- Character Count -------")
     
     for char_dict in sorted_count:
        character = char_dict["character"]
        count = char_dict["count"]
    
        if character.isalpha():
            print(f"{character}: {count}")
     print("============= END ===============")
     

main()