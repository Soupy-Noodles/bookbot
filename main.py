import sys
from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    print(f"Found {num_words} total words")
    # Only print alphabetical characters, sorted alphabetically
    for char in sorted(char_counts):
        if char.isalpha():
            print(f"{char}: {char_counts[char]}")

if __name__ == "__main__":
    main()