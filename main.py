def main():
    BOOK_PATH = "./books/frankenstein.txt"
    with open(BOOK_PATH) as book:
        book_contents = book.read()
        generate_report(book_contents)


def get_word_count(text):
    return len(text.split())

def generate_database(text):
    database = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter in database:
            database[lower_letter] += 1
        else:
            database[lower_letter] = 1
    return database


def generate_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_word_count(text)} words found in the document")
    database = generate_database(text)
    for key, value in sorted(database.items(), key=lambda entry: entry[1], reverse=True):
        if key.isalpha():
            print(f"The '{key}' character was found {value}")
    print("--- End report ---")
if __name__ == "__main__":
    main()

